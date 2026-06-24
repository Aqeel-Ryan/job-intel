# Job Intel

Job Intel helps job seekers make informed application decisions by predicting which Applicant Tracking System (ATS) a company uses, scoring their realistic chance of getting through the company's hiring process (0–100), surfacing interview intelligence (rounds, questions, difficulty) from public sources, and tracking applications in a kanban dashboard.

## System architecture

The backend is composed of three analysis modules fed by a layer of source scrapers, with a SQLite cache and an Anthropic-backed LLM client in between.

Data flows as follows. A request for a company triggers the **scrapers** — careers page, LinkedIn, Glassdoor, Crunchbase, and Reddit — each returning a raw signals dict. The **ATS Predictor** takes the careers-page and LinkedIn signals and classifies the company's ATS vendor: first by matching outbound job-posting URLs against a fingerprint table, then falling back to company-size-based tier inference. The **Interview Intel** module aggregates the Glassdoor and Reddit text and uses the LLM client to extract a structured interview report (rounds, difficulty, offer rate, questions). The **Chance Scorer** combines all of these — plus the applicant's resume and the job description — into a weighted 0–100 score with a per-signal breakdown. Results are assembled into a `CompanyProfile`, cached by company slug and date, and served to the React frontend over a FastAPI HTTP API. The frontend renders the ATS prediction, the chance gauge, the interview panel, and a kanban tracker for managing applications across stages.

Every configurable value — URLs, thresholds, weights, API keys, model parameters — lives in the root `config.py` and is overridable by environment variable. No module hardcodes these.

## Data sources

| Source | What it provides | Used by module | Rate limit / auth |
| --- | --- | --- | --- |
| Company careers page | Outbound job-posting URLs (ATS fingerprints), careers URL | ATS Predictor | None (polite crawl; shared user-agent) |
| LinkedIn | Employee count, industry, recent postings + apply URLs | ATS Predictor | RapidAPI proxy key (`RAPIDAPI_KEY`) |
| Glassdoor | Interview difficulty, offer rate, question texts | Interview Intel | None (scraped; user-agent + backoff) |
| Crunchbase | Revenue range, funding stage, headcount | Chance Scorer | API key (`CRUNCHBASE_API_KEY`) |
| Reddit | Interview-experience posts from relevant subreddits | Interview Intel | None (public JSON; user-agent + backoff) |
| Anthropic API | LLM extraction + summarisation | Interview Intel, LLM client | API key (`ANTHROPIC_API_KEY`) |

## ATS detection method

ATS detection runs in up to three layers, picking the highest-confidence result:

1. **URL fingerprinting** — the careers-page scraper collects every outbound job-posting URL. The ATS Predictor iterates `ATS_URL_FINGERPRINTS` (vendor → URL patterns) from config and matches the URLs against each vendor's patterns (e.g. `boards.greenhouse.io` → Greenhouse, `.myworkdayjobs.com` → Workday). This is the most reliable signal. Vendor names are never hardcoded in module code — they come entirely from the config table.
2. **Size inference fallback** — when no fingerprint matches, the predictor infers a likely ATS *tier* from employee headcount using `COMPANY_SIZE_TIER_MAP` and `ENTERPRISE_TIER_THRESHOLD`. Larger companies skew toward Tier 1 enterprise systems (Workday, Taleo, SAP).
3. **LLM extraction** — for ambiguous careers-page HTML, the `extract_ats` prompt asks the model to surface raw ATS signals (widget hostnames, form targets) which are then run back through the fingerprint matcher.

Each prediction carries a `tier` (1 = enterprise, 2 = mid-market, 3 = SMB) via `ATS_TIER_MAP`, which downstream drives both parse-risk and monoculture-risk scoring.

## Chance score model

The chance score is a weighted sum of eight independent signals, each scored 0.0–1.0 and multiplied by its weight (the weights sum to 1.0 and are validated on scorer init). The final score is scaled to 0–100 and bucketed into Reach / Match / Safe via the score thresholds.

| Signal | Weight | Data source | High score means / Low score means |
| --- | --- | --- | --- |
| `role_match` | 0.20 | Resume + job description | Resume closely matches the JD / poor keyword & skill overlap |
| `ats_parse_risk` | 0.15 | ATS prediction (tier) | Lenient ATS, resume parses cleanly / strict enterprise ATS likely to mis-parse |
| `glassdoor_offer_rate` | 0.15 | Glassdoor interview report | Company extends offers often / very selective |
| `interview_difficulty` | 0.10 | Glassdoor interview report | Easier reported process / notoriously hard interviews |
| `company_size_fit` | 0.10 | Crunchbase / LinkedIn headcount | Size band favourable to the applicant / poor fit |
| `funding_stage` | 0.10 | Crunchbase (`FUNDING_STAGE_SCORES`) | Growth-stage, actively hiring / unknown or contracting |
| `posting_recency` | 0.10 | LinkedIn posting date (`POSTING_RECENCY_SCORE_MAP`) | Freshly posted role / stale (>90 days) listing |
| `monoculture_risk` | 0.10 | ATS prediction (tier) | Low exposure to ATS monoculture filtering / high homogenisation risk |

## Monoculture risk

As more companies converge on a small number of enterprise ATS vendors, the screening logic applied to applicants becomes increasingly homogeneous — a candidate filtered out by one Tier 1 system's parsing or keyword heuristics is likely to be filtered out by every other company on the same platform, regardless of fit. This *algorithmic monoculture* effect is examined in Bommasani et al.'s Stanford FAccT '26 work on outcome homogenisation in automated decision systems: when many decision-makers rely on the same underlying model, individuals face *systemic exclusion* rather than a series of independent assessments. Job Intel surfaces this explicitly through the `monoculture_risk` signal, which weights an applicant's exposure by the predicted ATS tier — higher for the most widely-deployed enterprise systems — so users can see when a rejection is likely to generalise across employers and adjust their resume strategy (or target companies on less-saturated platforms) accordingly.

## Setup

```bash
# 1. Clone
git clone <repo-url> job-intel && cd job-intel

# 2. Configure environment
cp .env.example .env        # then fill in API keys

# 3. Backend (Python — pyenv + Poetry or a venv)
pip install -r requirements.txt
playwright install          # browser binaries for scraping

# 4. Frontend
cd frontend && npm install && cd ..

# 5. Run the backend (from the repo root, so `config` and `backend` import cleanly)
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# 6. Run the frontend (separate terminal)
cd frontend && npm run dev   # serves on http://localhost:5173
```

## Environment variables

Every variable below is defined in `config.py` with the default shown and is overridable via the environment (or `.env`).

| Variable | Default | Description |
| --- | --- | --- |
| `DEBUG` | `false` | Enable debug mode and backend autoreload |
| `ANTHROPIC_API_KEY` | `""` | Anthropic API key for the LLM client |
| `CRUNCHBASE_API_KEY` | `""` | Crunchbase API key (firmographics) |
| `RAPIDAPI_KEY` | `""` | RapidAPI key for the LinkedIn scraper proxy |
| `LLM_MODEL` | `claude-sonnet-4-6` | Model id used for all LLM calls |
| `LLM_MAX_TOKENS` | `2048` | Max output tokens per LLM call |
| `LLM_TEMPERATURE` | `0.2` | Sampling temperature |
| `REQUEST_TIMEOUT_S` | `15` | Per-request HTTP timeout (seconds) |
| `REQUEST_MAX_RETRIES` | `3` | Retries on transient HTTP failures |
| `REQUEST_BACKOFF_S` | `2.0` | Base backoff between retries (seconds) |
| `USER_AGENT` | `Mozilla/5.0 (compatible; JobIntelBot/1.0)` | Scraper user-agent |
| `CACHE_DB_PATH` | `cache/job_intel.db` | SQLite cache file path |
| `CACHE_TTL_HOURS` | `24` | Cache entry time-to-live (hours) |
| `BACKEND_HOST` | `0.0.0.0` | Backend bind host |
| `BACKEND_PORT` | `8000` | Backend bind port |
| `CORS_ORIGINS` | `http://localhost:5173` | Comma-separated allowed CORS origins |
| `SCORE_REACH_THRESHOLD` | `40` | Below this overall score → Reach |
| `SCORE_SAFE_THRESHOLD` | `70` | Above this overall score → Safe |
| `VITE_API_BASE_URL` | `http://localhost:8000` | Backend base URL the frontend calls |

Non-overridable config (base URLs, fingerprint/tier tables, score weights, funding/recency maps) also lives in `config.py` and is documented inline there.

## Phase roadmap

- **Phase 1 — this scaffold.** Full directory structure, typed signatures, docstrings, and config wiring. No business logic.
- **Phase 2 — resume upload + scoring.** Resume parsing and upload, live `role_match` scoring against the JD, real scraper and LLM implementations, populated cache.
- **Phase 3 — email alerts + multi-user.** Per-user accounts, saved companies, and email alerts on new postings / stage changes.

## Contributing

Keep it simple: one branch per feature, branched off `main`. Run linting and type checks before opening a PR (`ruff`/`mypy` for the backend, `tsc` for the frontend). Keep all configurable values in `config.py` — never hardcode URLs, thresholds, weights, or keys in a module.

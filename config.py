"""Job Intel — single source of truth for all runtime-configurable values.

Every module imports from here. No URLs, thresholds, weights, or API keys
are hardcoded anywhere else in the codebase. Every value is overridable via
environment variable using ``os.getenv`` with the default shown.
"""

import os

# ── App ──────────────────────────────────────────────────────────────────────
APP_NAME = "Job Intel"
APP_VERSION = "0.1.0"
DEBUG = bool(os.getenv("DEBUG", "false"))

# ── API keys ─────────────────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CRUNCHBASE_API_KEY = os.getenv("CRUNCHBASE_API_KEY", "")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")  # for LinkedIn scraper proxy

# ── LLM ──────────────────────────────────────────────────────────────────────
LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "2048"))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))

# ── Scraper ───────────────────────────────────────────────────────────────────
REQUEST_TIMEOUT_S = int(os.getenv("REQUEST_TIMEOUT_S", "15"))
REQUEST_MAX_RETRIES = int(os.getenv("REQUEST_MAX_RETRIES", "3"))
REQUEST_BACKOFF_S = float(os.getenv("REQUEST_BACKOFF_S", "2.0"))
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (compatible; JobIntelBot/1.0)")
GLASSDOOR_BASE_URL = "https://www.glassdoor.com"
LINKEDIN_BASE_URL = "https://www.linkedin.com"
CRUNCHBASE_BASE_URL = "https://api.crunchbase.com/api/v4"
REDDIT_BASE_URL = "https://www.reddit.com"

# ── ATS fingerprints (vendor → list of URL patterns) ────────────────────────
ATS_URL_FINGERPRINTS = {
    "Greenhouse": ["boards.greenhouse.io", "greenhouse.io/embed"],
    "Lever": ["jobs.lever.co", "lever.co/"],
    "Workday": [".myworkdayjobs.com", "wd1.myworkdayjobs", "wd3.myworkdayjobs"],
    "Taleo": [".taleo.net", "tbe.taleo.net"],
    "iCIMS": ["careers-", ".icims.com"],
    "Ashby": ["jobs.ashby.com", "ashbyhq.com"],
    "SmartRecruiters": ["jobs.smartrecruiters.com"],
    "Rippling": ["ats.rippling.com"],
    "BambooHR": [".bamboohr.com/jobs"],
    "Workable": ["apply.workable.com"],
    "HireVue": ["hirevue.com"],  # detected in JD text too
    "Jobvite": ["jobs.jobvite.com"],
    "SAP": ["jobs.sap.com", "successfactors"],
}

# ── ATS tier mapping (vendor → tier) ─────────────────────────────────────────
# Tier 1 = enterprise (Workday/Taleo/SAP) — strictest parsing, highest monoculture risk
# Tier 2 = mid-market (Greenhouse/iCIMS/Lever)
# Tier 3 = SMB (Ashby/BambooHR/Workable)
ATS_TIER_MAP = {
    "Workday": 1, "Taleo": 1, "SAP": 1, "iCIMS": 1,
    "Greenhouse": 2, "Lever": 2, "SmartRecruiters": 2, "Jobvite": 2,
    "Ashby": 3, "BambooHR": 3, "Workable": 3, "Rippling": 3,
}

# ── Company size → likely ATS tier ───────────────────────────────────────────
# (employee_count_max → tier)
COMPANY_SIZE_TIER_MAP = {
    50: 3,
    500: 2,
    5000: 2,
}
ENTERPRISE_TIER_THRESHOLD = 5000  # above this → tier 1

# ── Chance score weights (must sum to 1.0) ───────────────────────────────────
SCORE_WEIGHTS = {
    "role_match": 0.20,
    "ats_parse_risk": 0.15,
    "glassdoor_offer_rate": 0.15,
    "interview_difficulty": 0.10,
    "company_size_fit": 0.10,
    "funding_stage": 0.10,
    "posting_recency": 0.10,
    "monoculture_risk": 0.10,
}

# ── Funding stage scores (stage → raw score 0–1) ─────────────────────────────
FUNDING_STAGE_SCORES = {
    "seed": 0.6,
    "series_a": 0.75,
    "series_b": 0.8,
    "series_c": 0.85,
    "series_d+": 0.8,
    "public": 0.7,
    "bootstrapped": 0.65,
    "unknown": 0.5,
}

# ── Posting recency scoring (days_since_posted → score) ──────────────────────
POSTING_RECENCY_SCORE_MAP = {
    7: 1.0,
    30: 0.8,
    60: 0.5,
    90: 0.3,
}
POSTING_STALE_SCORE = 0.1  # older than 90 days

# ── Cache ────────────────────────────────────────────────────────────────────
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache/job_intel.db")
CACHE_TTL_HOURS = int(os.getenv("CACHE_TTL_HOURS", "24"))

# ── Backend server ────────────────────────────────────────────────────────────
BACKEND_HOST = os.getenv("BACKEND_HOST", "0.0.0.0")
BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000"))
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")

# ── Frontend ─────────────────────────────────────────────────────────────────
VITE_API_BASE_URL = os.getenv("VITE_API_BASE_URL", "http://localhost:8000")

# ── Score categories (backend mirror of frontend score.thresholds) ───────────
# Phase 2 will move these to the shared config consumed by both ends.
SCORE_CATEGORY_THRESHOLDS = {
    "reach": int(os.getenv("SCORE_REACH_THRESHOLD", "40")),  # below this → Reach
    "safe": int(os.getenv("SCORE_SAFE_THRESHOLD", "70")),    # above this → Safe; between → Match
}

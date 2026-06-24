// TypeScript interfaces mirroring the backend Pydantic models.
// Keep these in sync with backend/models/*.py.

export type DetectionMethod =
  | 'url_fingerprint'
  | 'size_inference'
  | 'llm_extraction'

export type ScoreCategory = 'Reach' | 'Match' | 'Safe'

export interface ATSPrediction {
  vendor: string
  confidence: number // 0.0–1.0
  tier: 1 | 2 | 3
  detection_method: DetectionMethod
  raw_signals: string[]
}

export interface SignalScore {
  name: string
  raw_score: number // 0.0–1.0
  weight: number
  weighted_contribution: number
  evidence: string
}

export interface ChanceScore {
  overall: number // 0–100
  breakdown: SignalScore[]
  category: ScoreCategory
  generated_at: string // ISO timestamp
}

export interface CompanyProfile {
  name: string
  slug: string
  employee_count: number | null
  revenue_range: string | null
  funding_stage: string | null
  industry: string | null
  hq_location: string | null
  careers_url: string | null
  ats_prediction: ATSPrediction | null
  chance_score: ChanceScore | null
  fetched_at: string // ISO timestamp
}

export type QuestionCategory =
  | 'behavioral'
  | 'technical'
  | 'situational'
  | 'culture'

export type QuestionSource = 'glassdoor' | 'reddit' | 'blind'

export type RoundFormat = 'phone' | 'video' | 'take_home' | 'onsite' | 'panel'

export interface Question {
  text: string
  category: QuestionCategory
  source: QuestionSource
}

export interface Round {
  name: string
  format: RoundFormat
  duration_minutes: number | null
  questions: Question[]
}

export interface InterviewReport {
  company_slug: string
  total_rounds: number
  difficulty_rating: number // 1.0–5.0
  offer_rate: number // 0.0–1.0
  avg_process_days: number | null
  rounds: Round[]
  raw_source_count: number
  fetched_at: string // ISO timestamp
}

export interface TrackedApplication {
  id: number
  company_slug: string
  role_title: string
  applied_date: string // ISO date
  stage: string
}

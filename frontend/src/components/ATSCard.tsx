// ATS prediction card: vendor, tier badge, confidence, detection method.

import type { ATSPrediction } from '../types'

export interface ATSCardProps {
  prediction: ATSPrediction
}

// What each tier means for resume formatting (shown to the user).
const TIER_DESCRIPTIONS: Record<1 | 2 | 3, string> = {
  1: 'Enterprise ATS — strict parsing. Use a plain, single-column resume; avoid tables, columns, and graphics.',
  2: 'Mid-market ATS — moderate parsing. Standard formatting is fine; keep section headers conventional.',
  3: 'SMB ATS — lenient parsing. More formatting latitude, but keep it clean and machine-readable.',
}

/** Placeholder card showing the predicted ATS vendor and what its tier implies. */
export function ATSCard({ prediction }: ATSCardProps) {
  return (
    <div>
      <h3>{prediction.vendor}</h3>
      <span>Tier {prediction.tier}</span>
      <span>{Math.round(prediction.confidence * 100)}% confidence</span>
      <p>Detected via: {prediction.detection_method}</p>
      <p>{TIER_DESCRIPTIONS[prediction.tier]}</p>
    </div>
  )
}

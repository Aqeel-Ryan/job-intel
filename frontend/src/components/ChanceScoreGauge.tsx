// 0–100 chance gauge with a colour-coded category label and signal breakdown.

import { config } from '../config'
import type { ChanceScore, ScoreCategory } from '../types'

export interface ChanceScoreGaugeProps {
  score: ChanceScore
}

// Derive the category bucket from the configured thresholds.
function categoryFor(overall: number): ScoreCategory {
  if (overall < config.score.thresholds.reach) return 'Reach'
  if (overall > config.score.thresholds.safe) return 'Safe'
  return 'Match'
}

const CATEGORY_COLORS: Record<ScoreCategory, string> = {
  Reach: '#e5484d', // red
  Match: '#f5a623', // amber
  Safe: '#30a46c',  // green
}

/** Placeholder gauge rendering the score, category label, and signal rows. */
export function ChanceScoreGauge({ score }: ChanceScoreGaugeProps) {
  const category = categoryFor(score.overall)

  return (
    <div>
      <div style={{ color: CATEGORY_COLORS[category] }}>
        <strong>{score.overall}</strong> / 100 — {category}
      </div>
      <ul>
        {score.breakdown.map((signal) => (
          <li key={signal.name}>
            <span>{signal.name}</span>
            <span>{signal.weighted_contribution.toFixed(2)}</span>
            <span>{signal.evidence}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}

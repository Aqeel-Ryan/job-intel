// Kanban board: one column per configured stage.

import { config } from '../config'
import type { TrackedApplication } from '../types'

export interface ApplicationTrackerProps {
  items: TrackedApplication[]
  /** Map of company slug → latest overall chance score, for display on cards. */
  scoresBySlug?: Record<string, number>
}

// Whole days since an ISO date string.
function daysSince(isoDate: string): number {
  const then = new Date(isoDate).getTime()
  return Math.floor((Date.now() - then) / (1000 * 60 * 60 * 24))
}

/** Placeholder kanban board, one column per `config.tracker.stages`. */
export function ApplicationTracker({
  items,
  scoresBySlug = {},
}: ApplicationTrackerProps) {
  return (
    <div style={{ display: 'flex', gap: '1rem' }}>
      {config.tracker.stages.map((stage) => (
        <div key={stage}>
          <h3>{stage}</h3>
          {items
            .filter((item) => item.stage === stage)
            .map((item) => (
              <div key={item.id}>
                <strong>{item.company_slug}</strong>
                <p>{item.role_title}</p>
                <p>{daysSince(item.applied_date)}d since applied</p>
                <p>Score: {scoresBySlug[item.company_slug] ?? '—'}</p>
              </div>
            ))}
        </div>
      ))}
    </div>
  )
}

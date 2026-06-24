// Fetches the chance-score breakdown for a company.

import { useState } from 'react'
import type { ChanceScore } from '../types'

export interface UseScoreResult {
  score: ChanceScore | null
  loading: boolean
  error: string | null
  /** Fetch (or recalculate, if JD/resume supplied) the score for a company slug. */
  fetch: (slug: string, jobDescription?: string, resumeText?: string) => Promise<void>
}

/**
 * Hook to fetch a company's chance score, exposing loading/error state.
 * Placeholder — wiring to `getScore` is implemented in a later phase.
 */
export function useScore(): UseScoreResult {
  const [score] = useState<ChanceScore | null>(null)
  const [loading] = useState(false)
  const [error] = useState<string | null>(null)

  async function fetch(
    _slug: string,
    _jobDescription?: string,
    _resumeText?: string,
  ): Promise<void> {
    // TODO: call getScore(slug, jobDescription, resumeText), set state.
  }

  return { score, loading, error, fetch }
}

// Fetches and caches a company profile from the backend.

import { useState } from 'react'
import type { CompanyProfile } from '../types'

export interface UseCompanyResult {
  profile: CompanyProfile | null
  loading: boolean
  error: string | null
  /** Trigger a fetch for the given company name. */
  fetch: (name: string) => Promise<void>
}

/**
 * Hook to fetch a company profile via the backend, exposing loading/error state.
 * Placeholder — wiring to `getCompany` is implemented in a later phase.
 */
export function useCompany(): UseCompanyResult {
  const [profile] = useState<CompanyProfile | null>(null)
  const [loading] = useState(false)
  const [error] = useState<string | null>(null)

  async function fetch(_name: string): Promise<void> {
    // TODO: call getCompany(name), set profile/loading/error.
  }

  return { profile, loading, error, fetch }
}

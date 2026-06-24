// CRUD state management for tracked applications.

import { useState } from 'react'
import type { TrackedApplication } from '../types'

export interface UseTrackerResult {
  items: TrackedApplication[]
  loading: boolean
  error: string | null
  refresh: () => Promise<void>
  create: (item: Omit<TrackedApplication, 'id'>) => Promise<void>
  updateStage: (id: number, stage: string) => Promise<void>
  remove: (id: number) => Promise<void>
}

/**
 * Hook managing the application tracker: list, create, update stage, delete.
 * Placeholder — wiring to the client API is implemented in a later phase.
 */
export function useTracker(): UseTrackerResult {
  const [items] = useState<TrackedApplication[]>([])
  const [loading] = useState(false)
  const [error] = useState<string | null>(null)

  async function refresh(): Promise<void> {
    // TODO: getTrackerItems()
  }
  async function create(_item: Omit<TrackedApplication, 'id'>): Promise<void> {
    // TODO: createTrackerItem(item) then refresh
  }
  async function updateStage(_id: number, _stage: string): Promise<void> {
    // TODO: updateTrackerStage(id, stage) then refresh
  }
  async function remove(_id: number): Promise<void> {
    // TODO: deleteTrackerItem(id) then refresh
  }

  return { items, loading, error, refresh, create, updateStage, remove }
}

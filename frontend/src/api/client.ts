// Axios instance and typed API functions pointed at the backend base URL.

import axios from 'axios'
import { config } from '../config'
import type {
  ChanceScore,
  CompanyProfile,
  TrackedApplication,
} from '../types'

export const api = axios.create({
  baseURL: config.apiBaseUrl,
})

/** Fetch the full company profile (runs the pipeline / returns cached). */
export async function getCompany(name: string): Promise<CompanyProfile> {
  // TODO: GET /company/{name}
  throw new Error('Not implemented')
}

/** Fetch the chance-score breakdown, optionally recalculating against a JD/resume. */
export async function getScore(
  slug: string,
  jobDescription?: string,
  resumeText?: string,
): Promise<ChanceScore> {
  // TODO: GET /score/{slug}, or POST /score/{slug}/recalculate when JD/resume given.
  throw new Error('Not implemented')
}

/** List all tracked applications. */
export async function getTrackerItems(): Promise<TrackedApplication[]> {
  // TODO: GET /tracker
  throw new Error('Not implemented')
}

/** Create a tracked application. */
export async function createTrackerItem(
  item: Omit<TrackedApplication, 'id'>,
): Promise<TrackedApplication> {
  // TODO: POST /tracker
  throw new Error('Not implemented')
}

/** Update the kanban stage of a tracked application. */
export async function updateTrackerStage(
  id: number,
  stage: string,
): Promise<TrackedApplication> {
  // TODO: PATCH /tracker/{id}
  throw new Error('Not implemented')
}

/** Delete a tracked application. */
export async function deleteTrackerItem(id: number): Promise<void> {
  // TODO: DELETE /tracker/{id}
  throw new Error('Not implemented')
}

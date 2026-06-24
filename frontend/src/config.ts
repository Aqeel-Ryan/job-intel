export const config = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000',
  appName: 'Job Intel',
  version: '0.1.0',
  features: {
    redditIntel: true,
    monocultureRisk: true,
    resumeUpload: false,     // Phase 2
    emailAlerts: false,      // Phase 2
  },
  tracker: {
    stages: ['Saved', 'Applied', 'Screening', 'Interview', 'Offer', 'Rejected'],
    defaultStage: 'Saved',
  },
  score: {
    thresholds: {
      reach: 40,   // below 40 = Reach
      safe: 70,    // above 70 = Safe, between = Match
    },
  },
} as const

// Accordion of interview intelligence: overall stats, rounds, top questions.

import type { InterviewReport, QuestionCategory } from '../types'

export interface InterviewIntelPanelProps {
  report: InterviewReport
}

const QUESTION_CATEGORIES: QuestionCategory[] = [
  'behavioral',
  'technical',
  'situational',
  'culture',
]

/** Placeholder accordion summarising the interview report. */
export function InterviewIntelPanel({ report }: InterviewIntelPanelProps) {
  return (
    <div>
      <section>
        <h3>Overview</h3>
        <p>Rounds: {report.total_rounds}</p>
        <p>Difficulty: {report.difficulty_rating.toFixed(1)} / 5</p>
        <p>Offer rate: {Math.round(report.offer_rate * 100)}%</p>
        <p>Avg process: {report.avg_process_days ?? '—'} days</p>
      </section>

      <section>
        <h3>Rounds</h3>
        <ol>
          {report.rounds.map((round, i) => (
            <li key={i}>
              {round.name} — {round.format}
              {round.duration_minutes ? ` (${round.duration_minutes}m)` : ''}
            </li>
          ))}
        </ol>
      </section>

      <section>
        <h3>Top questions by category</h3>
        {QUESTION_CATEGORIES.map((category) => (
          <div key={category}>
            <h4>{category}</h4>
            <ul>
              {report.rounds
                .flatMap((r) => r.questions)
                .filter((q) => q.category === category)
                .map((q, i) => (
                  <li key={i}>{q.text}</li>
                ))}
            </ul>
          </div>
        ))}
      </section>
    </div>
  )
}

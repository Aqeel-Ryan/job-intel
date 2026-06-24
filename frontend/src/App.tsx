// Root application component. Placeholder layout wiring the search bar,
// company analysis panels, and the application tracker together.

import { ApplicationTracker } from './components/ApplicationTracker'
import { ATSCard } from './components/ATSCard'
import { ChanceScoreGauge } from './components/ChanceScoreGauge'
import { CompanySearch } from './components/CompanySearch'
import { InterviewIntelPanel } from './components/InterviewIntelPanel'
import { config } from './config'
import { useCompany } from './hooks/useCompany'
import { useTracker } from './hooks/useTracker'

export default function App() {
  const { profile, fetch } = useCompany()
  const { items } = useTracker()

  return (
    <main>
      <header>
        <h1>{config.appName}</h1>
        <span>v{config.version}</span>
      </header>

      <CompanySearch onSearch={fetch} />

      {profile && (
        <section>
          <h2>{profile.name}</h2>
          {profile.ats_prediction && (
            <ATSCard prediction={profile.ats_prediction} />
          )}
          {profile.chance_score && (
            <ChanceScoreGauge score={profile.chance_score} />
          )}
          {/* InterviewIntelPanel is rendered once an InterviewReport is wired in. */}
          {false && <InterviewIntelPanel report={undefined as never} />}
        </section>
      )}

      <section>
        <h2>Tracker</h2>
        <ApplicationTracker items={items} />
      </section>
    </main>
  )
}

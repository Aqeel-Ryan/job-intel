// Search bar + trigger for looking up a company.

import { useState } from 'react'

export interface CompanySearchProps {
  /** Called with the entered company name when the user submits. */
  onSearch: (name: string) => void
}

/** Placeholder search bar — emits the entered company name on submit. */
export function CompanySearch({ onSearch }: CompanySearchProps) {
  const [name, setName] = useState('')

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        if (name.trim()) onSearch(name.trim())
      }}
    >
      <input
        type="text"
        value={name}
        placeholder="Company name…"
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Analyze</button>
    </form>
  )
}

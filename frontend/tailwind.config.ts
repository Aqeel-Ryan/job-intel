import type { Config } from 'tailwindcss'

// Tailwind scans the index.html and all source files for class names.
const config: Config = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
}

export default config

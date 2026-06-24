import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite config for the Job Intel frontend. The dev server runs on port 5173,
// which is the default allowed CORS origin on the backend.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
})

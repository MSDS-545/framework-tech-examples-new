// The React plugin lets Vite transform JSX and support React development tools.
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
export default defineConfig({ plugins: [react()] })

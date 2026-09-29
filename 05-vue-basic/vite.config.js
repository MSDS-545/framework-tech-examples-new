// Vite is the development/build tool. The Vue plugin teaches Vite how to
// compile .vue Single-File Components containing <script>, <template>, etc.
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig({ plugins: [vue()] })

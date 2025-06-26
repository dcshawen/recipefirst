import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
		tailwindcss(),	
	],
	  server: {
    host: true,           // listen on all addresses, not just localhost
    port: 5173,           // default port
    open: true,           // auto-open in browser
    hmr: { overlay: true},// show errors in-page
    watch: {
      // only needed in Docker/WSL; polling solves “no changes detected”
      usePolling: true,
      interval: 100
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})

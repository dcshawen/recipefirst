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
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: '0.0.0.0',
    allowedHosts: [
      "ec2-16-52-119-18.ca-central-1.compute.amazonaws.com",
			"16.52.119.18",
			"r3cipe.com"
    ],
    watch: {
      usePolling: true
    },
    proxy: {
      '/api': {
        // Use environment variable when set (useful for local dev override),
        // otherwise default to the Docker Compose service hostname used in containers.
        target: process.env.VITE_DEV_API_TARGET || 'http://fastapi:8000',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
  }
})

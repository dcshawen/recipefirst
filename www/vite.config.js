import { fileURLToPath, URL } from 'node:url'
import fs from 'fs'
import path from 'path'

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
    // Optional HTTPS dev server: place certs in ./certs (see README instructions)
    // If cert files are missing, Vite will fall back to HTTP.
    const __filename = fileURLToPath(import.meta.url)
    const __dirname = path.dirname(__filename)
    const certDir = path.resolve(__dirname, 'certs')
    const keyPath = path.join(certDir, 'localhost-key.pem')
    const certPath = path.join(certDir, 'localhost.pem')
    const httpsConfig = (fs.existsSync(keyPath) && fs.existsSync(certPath))
      ? { key: fs.readFileSync(keyPath), cert: fs.readFileSync(certPath) }
      : false

    host: '0.0.0.0',
    https: httpsConfig,
    allowedHosts: [
      "ec2-16-52-119-18.ca-central-1.compute.amazonaws.com",
			"16.52.119.18"
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

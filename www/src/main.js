import { createApp, ref, watch } from 'vue'
import router from './routes.js'
import App from './App.vue'

// Theme logic
const storedTheme = localStorage.getItem('theme')
const isDark = ref(storedTheme ? storedTheme === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches)
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)')

const applyTheme = (dark) => {
  if (dark) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

// Initial application of theme
applyTheme(isDark.value)

// Watch for changes to isDark and update
watch(isDark, (newVal) => {
  applyTheme(newVal)
})

// Keep in sync with system theme until user explicitly sets one
systemPrefersDark.addEventListener('change', (event) => {
  if (!localStorage.getItem('theme')) {
    isDark.value = event.matches
  }
})

const app = createApp(App)
app.use(router)

// Provide theme state and toggle function
app.provide('isDark', isDark)
app.provide('toggleTheme', () => {
  isDark.value = !isDark.value
})

app.mount('#app')

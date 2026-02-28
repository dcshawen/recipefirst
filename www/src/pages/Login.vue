<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
    <div class="w-full max-w-sm bg-white rounded-2xl shadow-lg p-8">
      <!-- Logo -->
      <div class="flex flex-col items-center mb-8">
        <i class="mdi mdi-chef-hat text-5xl text-brand-700 mb-2"></i>
        <h1 class="text-2xl font-bold text-gray-800 tracking-tight">RecipeFirst</h1>
        <p class="text-sm text-gray-500 mt-1">Sign in to continue</p>
      </div>

      <!-- Error banner -->
      <div
        v-if="error"
        class="mb-4 rounded-lg bg-red-50 border border-red-200 px-4 py-3 text-sm text-red-700 flex items-center gap-2"
        role="alert"
      >
        <i class="mdi mdi-alert-circle-outline text-base"></i>
        {{ error }}
      </div>

      <!-- Login form -->
      <form class="space-y-4" @submit.prevent="handleSubmit">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-1">
            Username
          </label>
          <input
            id="username"
            v-model="username"
            type="text"
            autocomplete="username"
            required
            :disabled="loading"
            class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent disabled:bg-gray-100"
            placeholder="Enter your username"
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">
            Password
          </label>
          <input
            id="password"
            v-model="password"
            type="password"
            autocomplete="current-password"
            required
            :disabled="loading"
            class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent disabled:bg-gray-100"
            placeholder="Enter your password"
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full flex items-center justify-center gap-2 rounded-lg bg-brand-700 hover:bg-brand-800 text-white font-semibold py-2.5 text-sm transition-colors disabled:opacity-60 disabled:cursor-not-allowed"
        >
          <i v-if="loading" class="mdi mdi-loading animate-spin text-base"></i>
          <i v-else class="mdi mdi-login text-base"></i>
          {{ loading ? 'Signing in…' : 'Sign in' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuth } from '../composables/useAuth.js'

const router = useRouter()
const route = useRoute()
const { login } = useAuth()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref(null)

async function handleSubmit() {
  error.value = null
  loading.value = true

  try {
    await login({ username: username.value, password: password.value })
    // Redirect to the originally requested page, or home.
    const redirect = route.query.redirect || '/'
    router.push(redirect)
  } catch (err) {
    error.value = err.message || 'Invalid username or password.'
  } finally {
    loading.value = false
  }
}
</script>

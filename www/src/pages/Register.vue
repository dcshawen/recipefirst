<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
    <div class="w-full max-w-sm bg-white rounded-2xl shadow-lg p-8">
      <!-- Logo -->
      <div class="flex flex-col items-center mb-8">
        <i class="mdi mdi-chef-hat text-5xl text-brand-700 mb-2"></i>
        <h1 class="text-2xl font-bold text-gray-800 tracking-tight">RecipeFirst</h1>
        <p class="text-sm text-gray-500 mt-1">Create an account</p>
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

      <!-- Registration form -->
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
            placeholder="Choose a username"
          />
        </div>

        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">
            Email
          </label>
          <input
            id="email"
            v-model="email"
            type="email"
            autocomplete="email"
            required
            :disabled="loading"
            class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent disabled:bg-gray-100"
            placeholder="Enter your email"
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
            autocomplete="new-password"
            required
            :disabled="loading"
            class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent disabled:bg-gray-100"
            placeholder="Create a password"
          />
        </div>

        <div>
          <label for="confirm-password" class="block text-sm font-medium text-gray-700 mb-1">
            Confirm Password
          </label>
          <input
            id="confirm-password"
            v-model="confirmPassword"
            type="password"
            autocomplete="new-password"
            required
            :disabled="loading"
            class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent disabled:bg-gray-100"
            placeholder="Repeat your password"
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full flex items-center justify-center gap-2 rounded-lg bg-brand-700 hover:bg-brand-800 text-white font-semibold py-2.5 text-sm transition-colors disabled:opacity-60 disabled:cursor-not-allowed"
        >
          <i v-if="loading" class="mdi mdi-loading animate-spin text-base"></i>
          <i v-else class="mdi mdi-account-plus text-base"></i>
          {{ loading ? 'Creating account…' : 'Create account' }}
        </button>
      </form>

      <p class="mt-6 text-center text-sm text-gray-500">
        Already have an account?
        <router-link to="/login" class="text-brand-700 font-medium hover:underline">Sign in</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth.js'

const router = useRouter()
const { register } = useAuth()

const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const error = ref(null)

async function handleSubmit() {
  error.value = null

  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match.'
    return
  }

  loading.value = true

  try {
    await register({ username: username.value, email: email.value, password: password.value })
    // Account created – send the user to login.
    router.push('/login')
  } catch (err) {
    error.value = err.message || 'Registration failed. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

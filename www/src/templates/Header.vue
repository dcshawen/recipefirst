<template>
  <div class="sticky top-0 z-30 shadow-md">
    <header class="bg-brand-900 text-white">
      <div class="flex items-center gap-3 px-4 py-3 lg:px-6">
        <!-- Mobile menu toggle -->
        <button
          class="lg:hidden btn-icon text-white/80 hover:text-white hover:bg-white/10 rounded-lg transition-colors"
          aria-label="Toggle menu"
          @click="$emit('toggle-sidebar')"
        >
          <i class="mdi mdi-menu text-xl"></i>
        </button>

        <!-- Logo / Title -->
        <router-link to="/" class="flex items-center gap-2 text-white no-underline shrink-0">
          <i class="mdi mdi-chef-hat text-2xl text-brand-300"></i>
          <span class="text-lg font-bold tracking-tight">RecipeFirst</span>
        </router-link>

        <!-- Spacer -->
        <div class="flex-1"></div>

        <!-- Search -->
        <OmniSearch />

        <!-- Logout -->
        <button
          v-if="isAuthenticated"
          class="ml-2 btn-icon text-white/80 hover:text-white hover:bg-white/10 rounded-lg transition-colors flex items-center gap-1 px-2 py-1 text-sm"
          aria-label="Log out"
          title="Log out"
          @click="handleLogout"
        >
          <i class="mdi mdi-logout text-lg"></i>
          <span class="hidden sm:inline">Log out</span>
        </button>
      </div>
    </header>
    <!-- Breadcrumbs -->
    <div class="bg-white border-b border-gray-200 px-4 py-2 lg:px-6 hidden sm:block">
      <Breadcrumbs />
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import OmniSearch from '../components/OmniSearch.vue'
import Breadcrumbs from '../components/Breadcrumbs.vue'
import { useAuth } from '../composables/useAuth.js'

const router = useRouter()
const { isAuthenticated, logout } = useAuth()

function handleLogout() {
  logout()
  router.push('/login')
}

defineEmits(['toggle-sidebar'])
</script>
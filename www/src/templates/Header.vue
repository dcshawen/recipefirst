<template>
  <header class="sticky top-0 z-30 bg-brand-900 text-white shadow-md">
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
    </div>
  </header>
</template>

<script setup>
import OmniSearch from '../components/OmniSearch.vue'

defineEmits(['toggle-sidebar'])
</script>
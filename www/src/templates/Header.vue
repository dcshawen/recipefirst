<template>
  <div class="bg-blue-950 text-white pa-4">
    <div class="flex items-center justify-between gap-4">
      <!-- Title - Left aligned -->
      <h1 class="text-lg font-bold whitespace-nowrap">RecipeFirst</h1>

      <!-- Search bar - Center aligned with flex grow -->
      <div class="flex-grow flex justify-end">
        <OmniSearch/>
      </div>

      <!-- Spacer for balance - hidden on small screens -->
      <div class="hidden md:block" style="width: 120px;"></div>
    </div>
  </div>
</template>

<script setup>
import OmniSearch from '../components/OmniSearch.vue'
</script>
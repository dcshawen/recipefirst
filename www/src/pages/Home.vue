<template>
  <div class="page-container">
    <!-- Hero section -->
    <div class="mb-8">
      <h1 class="text-2xl sm:text-3xl font-bold text-gray-900 mb-1">Welcome to RecipeFirst</h1>
      <p class="text-gray-500">Your one-stop solution for all your recipe needs.</p>
    </div>

    <!-- Quick-action cards -->
    <h2 class="section-title">Quick Actions</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
      <router-link
        v-for="action in quickActions"
        :key="action.to"
        :to="action.to"
        class="card flex items-center gap-4 p-5 hover:shadow-md transition-shadow no-underline group"
      >
        <div class="flex items-center justify-center w-11 h-11 rounded-lg bg-brand-50 text-brand-600 group-hover:bg-brand-100 transition-colors">
          <i :class="['mdi', action.icon, 'text-xl']"></i>
        </div>
        <div>
          <p class="text-sm font-semibold text-gray-900">{{ action.label }}</p>
          <p class="text-xs text-gray-500">{{ action.desc }}</p>
        </div>
      </router-link>
    </div>

    <!-- Browse section -->
    <h2 class="section-title">Browse</h2>
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
      <router-link
        v-for="link in browseLinks"
        :key="link.to"
        :to="link.to"
        class="card p-4 text-center hover:shadow-md transition-shadow no-underline group"
      >
        <i :class="['mdi', link.icon, 'text-2xl text-gray-400 group-hover:text-brand-600 transition-colors']"></i>
        <p class="mt-1 text-sm font-medium text-gray-700">{{ link.label }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
const quickActions = [
  { to: '/recipes/create', icon: 'mdi-plus-circle-outline', label: 'New Recipe', desc: 'Create a new recipe' },
  { to: '/meals/create',   icon: 'mdi-silverware-fork-knife', label: 'New Meal', desc: 'Plan a new meal' },
  { to: '/fooditems/create', icon: 'mdi-food-apple-outline', label: 'New Food Item', desc: 'Add a food item' },
]

const browseLinks = [
  { to: '/recipes',     icon: 'mdi-food',                  label: 'Recipes' },
  { to: '/meals',       icon: 'mdi-silverware-fork-knife',  label: 'Meals' },
  { to: '/fooditems',   icon: 'mdi-food-apple-outline',     label: 'Food Items' },
  { to: '/ingredients', icon: 'mdi-grain',                  label: 'Ingredients' },
  { to: '/categories',  icon: 'mdi-tag-outline',            label: 'Categories' },
  { to: '/unittypes',   icon: 'mdi-scale-balance',          label: 'Units' },
]
</script>
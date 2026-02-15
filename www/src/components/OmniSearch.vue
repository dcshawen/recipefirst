<template>
  <div class="relative w-full max-w-[400px]" ref="wrapperRef">
    <!-- Search Input -->
    <div class="relative">
      <i class="mdi mdi-magnify absolute left-3 top-1/2 -translate-y-1/2 text-white/50"></i>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search everything…"
        class="w-full pl-9 pr-8 py-2 rounded-lg text-sm bg-white/15 text-white placeholder-white/50 border border-white/20 focus:outline-none focus:bg-white/25 focus:border-white/40 transition-colors"
      />
      <button
        v-if="searchQuery"
        @click="handleClear"
        class="absolute right-2 top-1/2 -translate-y-1/2 text-white/50 hover:text-white"
        aria-label="Clear search"
      >
        <i class="mdi mdi-close text-sm"></i>
      </button>
    </div>

    <!-- Loading indicator -->
    <div v-if="isSearching && searchQuery" class="dropdown p-3 text-sm text-gray-500">
      <span class="inline-flex items-center gap-2"><i class="mdi mdi-loading mdi-spin"></i> Searching…</span>
    </div>

    <!-- Results Dropdown -->
    <div
      v-if="isMenuOpen && showResults && !isSearching"
      class="dropdown max-h-[480px]"
    >
      <!-- No results message -->
      <div v-if="getTotalResults() === 0 && searchQuery.length > 0" class="px-4 py-3 text-sm text-gray-500">
        No results found for "{{ searchQuery }}"
      </div>

      <!-- Recipes -->
      <template v-if="searchResults.recipes.length > 0">
        <p class="px-4 pt-3 pb-1 text-xs font-semibold uppercase tracking-wider text-gray-400">Recipes</p>
        <button
          v-for="recipe in searchResults.recipes"
          :key="`recipe-${recipe.recipe_id}`"
          @click="navigateTo('/recipes', recipe.recipe_id)"
          class="dropdown-item flex items-center gap-3"
        >
          <i class="mdi mdi-food text-brand-600"></i>
          <div>
            <div class="text-sm font-medium text-gray-900">{{ recipe.recipe_name }}</div>
            <div v-if="recipe.recipe_description" class="text-xs text-gray-500">{{ truncate(recipe.recipe_description, 80) }}</div>
          </div>
        </button>
      </template>

      <!-- Meals -->
      <template v-if="searchResults.meals.length > 0">
        <hr v-if="searchResults.recipes.length > 0" class="border-gray-100" />
        <p class="px-4 pt-3 pb-1 text-xs font-semibold uppercase tracking-wider text-gray-400">Meals</p>
        <button
          v-for="meal in searchResults.meals"
          :key="`meal-${meal.meal_id}`"
          @click="navigateTo('/meals', meal.meal_id)"
          class="dropdown-item flex items-center gap-3"
        >
          <i class="mdi mdi-silverware-fork-knife text-accent-600"></i>
          <div>
            <div class="text-sm font-medium text-gray-900">{{ meal.meal_name }}</div>
            <div v-if="meal.meal_description" class="text-xs text-gray-500">{{ truncate(meal.meal_description, 80) }}</div>
          </div>
        </button>
      </template>

      <!-- Food Items -->
      <template v-if="searchResults.food_items.length > 0">
        <hr v-if="searchResults.recipes.length > 0 || searchResults.meals.length > 0" class="border-gray-100" />
        <p class="px-4 pt-3 pb-1 text-xs font-semibold uppercase tracking-wider text-gray-400">Food Items</p>
        <button
          v-for="foodItem in searchResults.food_items"
          :key="`fooditem-${foodItem.fooditem_id}`"
          @click="navigateTo('/fooditems', foodItem.fooditem_id)"
          class="dropdown-item flex items-center gap-3"
        >
          <i class="mdi mdi-food-apple text-amber-600"></i>
          <div>
            <div class="text-sm font-medium text-gray-900">{{ foodItem.fooditem_name }}</div>
            <div v-if="foodItem.fooditem_description" class="text-xs text-gray-500">{{ truncate(foodItem.fooditem_description, 80) }}</div>
          </div>
        </button>
      </template>

      <!-- Ingredients -->
      <template v-if="searchResults.ingredients.length > 0">
        <hr v-if="getTotalResults() > searchResults.ingredients.length" class="border-gray-100" />
        <p class="px-4 pt-3 pb-1 text-xs font-semibold uppercase tracking-wider text-gray-400">Ingredients</p>
        <button
          v-for="ingredient in searchResults.ingredients"
          :key="`ingredient-${ingredient.ingredient_id}`"
          @click="navigateTo('/ingredients', ingredient.ingredient_id)"
          class="dropdown-item flex items-center gap-3"
        >
          <i class="mdi mdi-grain text-cyan-600"></i>
          <div>
            <div class="text-sm font-medium text-gray-900">{{ ingredient.ingredient_name }}</div>
            <div v-if="ingredient.ingredient_description" class="text-xs text-gray-500">{{ truncate(ingredient.ingredient_description, 80) }}</div>
          </div>
        </button>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useSearch } from '../composables/useSearch'
import { useDebounce } from '../composables/useDebounce'

const router = useRouter()
const { isSearching, searchResults, search, clearSearch, getTotalResults } = useSearch()

const searchQuery = ref('')
const debouncedQuery = useDebounce(searchQuery, 300)
const isMenuOpen = ref(false)
const wrapperRef = ref(null)

// Show results when there's a query and results available
const showResults = computed(() => {
  return searchQuery.value.length > 0 && (getTotalResults() > 0 || !isSearching.value)
})

// Watch debounced query and perform search
watch(debouncedQuery, async (newQuery) => {
  if (newQuery && newQuery.trim().length > 0) {
    await search(newQuery)
    isMenuOpen.value = true
  } else {
    clearSearch()
    isMenuOpen.value = false
  }
})

// Close dropdown on click outside
function handleClickOutside(event) {
  if (wrapperRef.value && !wrapperRef.value.contains(event.target)) {
    isMenuOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Navigate to detail page and close menu
const navigateTo = (route, id) => {
  router.push(`${route}/${id}`)
  searchQuery.value = ''
  isMenuOpen.value = false
  clearSearch()
}

// Handle clear button
const handleClear = () => {
  searchQuery.value = ''
  clearSearch()
  isMenuOpen.value = false
}

// Utility to truncate long descriptions
const truncate = (text, maxLength) => {
  if (!text) return ''
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text
}
</script>

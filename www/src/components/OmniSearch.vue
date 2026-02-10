<template>
  <div class="omni-search-wrapper">
    <v-menu
      v-model="isMenuOpen"
      :close-on-content-click="false"
      location="bottom"
      offset="4"
      max-width="600"
      max-height="500"
    >
      <template v-slot:activator="{ props }">
        <v-text-field
          v-model="searchQuery"
          v-bind="props"
          placeholder="Search recipes, meals, food items, ingredients..."
          prepend-inner-icon="mdi-magnify"
          variant="outlined"
          density="compact"
          hide-details
          clearable
          @click:clear="handleClear"
          :loading="isSearching"
          class="omni-search-field"
        ></v-text-field>
      </template>

      <v-card v-if="showResults" max-height="480" class="overflow-y-auto">
        <v-list>
          <!-- No results message -->
          <v-list-item v-if="getTotalResults() === 0 && searchQuery.length > 0 && !isSearching">
            <v-list-item-title class="text-grey">
              No results found for "{{ searchQuery }}"
            </v-list-item-title>
          </v-list-item>

          <!-- Recipes -->
          <template v-if="searchResults.recipes.length > 0">
            <v-list-subheader>Recipes</v-list-subheader>
            <v-list-item
              v-for="recipe in searchResults.recipes"
              :key="`recipe-${recipe.recipe_id}`"
              @click="navigateTo('/recipes', recipe.recipe_id)"
              class="cursor-pointer"
            >
              <template v-slot:prepend>
                <v-icon color="primary">mdi-food</v-icon>
              </template>
              <v-list-item-title>{{ recipe.recipe_name }}</v-list-item-title>
              <v-list-item-subtitle v-if="recipe.recipe_description">
                {{ truncate(recipe.recipe_description, 80) }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>

          <!-- Meals -->
          <template v-if="searchResults.meals.length > 0">
            <v-divider v-if="searchResults.recipes.length > 0"></v-divider>
            <v-list-subheader>Meals</v-list-subheader>
            <v-list-item
              v-for="meal in searchResults.meals"
              :key="`meal-${meal.meal_id}`"
              @click="navigateTo('/meals', meal.meal_id)"
              class="cursor-pointer"
            >
              <template v-slot:prepend>
                <v-icon color="success">mdi-silverware</v-icon>
              </template>
              <v-list-item-title>{{ meal.meal_name }}</v-list-item-title>
              <v-list-item-subtitle v-if="meal.meal_description">
                {{ truncate(meal.meal_description, 80) }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>

          <!-- Food Items -->
          <template v-if="searchResults.food_items.length > 0">
            <v-divider v-if="searchResults.recipes.length > 0 || searchResults.meals.length > 0"></v-divider>
            <v-list-subheader>Food Items</v-list-subheader>
            <v-list-item
              v-for="foodItem in searchResults.food_items"
              :key="`fooditem-${foodItem.fooditem_id}`"
              @click="navigateTo('/fooditems', foodItem.fooditem_id)"
              class="cursor-pointer"
            >
              <template v-slot:prepend>
                <v-icon color="warning">mdi-food-apple</v-icon>
              </template>
              <v-list-item-title>{{ foodItem.fooditem_name }}</v-list-item-title>
              <v-list-item-subtitle v-if="foodItem.fooditem_description">
                {{ truncate(foodItem.fooditem_description, 80) }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>

          <!-- Ingredients -->
          <template v-if="searchResults.ingredients.length > 0">
            <v-divider v-if="getTotalResults() > searchResults.ingredients.length"></v-divider>
            <v-list-subheader>Ingredients</v-list-subheader>
            <v-list-item
              v-for="ingredient in searchResults.ingredients"
              :key="`ingredient-${ingredient.ingredient_id}`"
              @click="navigateTo('/ingredients', ingredient.ingredient_id)"
              class="cursor-pointer"
            >
              <template v-slot:prepend>
                <v-icon color="info">mdi-nutrition</v-icon>
              </template>
              <v-list-item-title>{{ ingredient.ingredient_name }}</v-list-item-title>
              <v-list-item-subtitle v-if="ingredient.ingredient_description">
                {{ truncate(ingredient.ingredient_description, 80) }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-menu>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useSearch } from '../composables/useSearch'
import { useDebounce } from '../composables/useDebounce'

const router = useRouter()
const { isSearching, searchResults, search, clearSearch, getTotalResults } = useSearch()

const searchQuery = ref('')
const debouncedQuery = useDebounce(searchQuery, 300)
const isMenuOpen = ref(false)

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

<style scoped>
.omni-search-wrapper {
  width: 100%;
  max-width: 400px;
}

.omni-search-field {
  background-color: white;
	color: black;
}

.cursor-pointer {
  cursor: pointer;
}

.cursor-pointer:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
</style>

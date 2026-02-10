import { ref } from 'vue'

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

export function useSearch() {
  const isSearching = ref(false)
  const searchError = ref(null)
  const searchResults = ref({
    recipes: [],
    meals: [],
    food_items: [],
    ingredients: []
  })

  /**
   * Perform search across all entity types
   * @param {string} query - Search query string
   */
  const search = async (query) => {
    if (!query || query.trim().length === 0) {
      searchResults.value = {
        recipes: [],
        meals: [],
        food_items: [],
        ingredients: []
      }
      return
    }

    isSearching.value = true
    searchError.value = null

    try {
      const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`)

      if (!response.ok) {
        throw new Error(`Search failed: ${response.status}`)
      }

      const data = await response.json()
      searchResults.value = data.results || {
        recipes: [],
        meals: [],
        food_items: [],
        ingredients: []
      }
    } catch (err) {
      searchError.value = err.message
      console.error('Search error:', err)
    } finally {
      isSearching.value = false
    }
  }

  /**
   * Clear search results
   */
  const clearSearch = () => {
    searchResults.value = {
      recipes: [],
      meals: [],
      food_items: [],
      ingredients: []
    }
    searchError.value = null
  }

  /**
   * Get total result count across all types
   */
  const getTotalResults = () => {
    return (
      searchResults.value.recipes.length +
      searchResults.value.meals.length +
      searchResults.value.food_items.length +
      searchResults.value.ingredients.length
    )
  }

  return {
    isSearching,
    searchError,
    searchResults,
    search,
    clearSearch,
    getTotalResults
  }
}

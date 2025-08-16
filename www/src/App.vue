<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Header from './templates/Header.vue'
import MainMenu from './templates/MainMenu.vue'
import Footer from './templates/Footer.vue'
import ItemDetails from './pages/ItemDetails.vue'

// Base URL for API; set VITE_API_BASE in your env (e.g., http://localhost:8000)
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const router = useRouter()

function getColumns(obj) {
  return Object.keys(obj).map(key => ({
    field: key,
    label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
  })).slice(1);
}

const itemData = ref({
  item: null,
  columns: []
})
const isLoading = ref(false)

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`)
  return res.json()
}

async function showHome() {
 router.push('/') 
}

async function showIngredients() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/ingredients')
    const list = data?.ingredients ?? []
    if (!Array.isArray(list) || list.length === 0) return
		const columns = getColumns(list[0]).filter(col => {
			return col.field !== 'ingredient_description' && col.field !== 'ingredient_notes'
		})
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/ingredients`)
  } catch (e) {
    console.error('Failed to fetch ingredients', e)
  } finally {
    isLoading.value = false
  }
}

async function showRecipes() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/recipes')
    const list = data?.recipes ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0]).filter(col => {
      return col.field !== 'ingredients' && col.field !== 'instructions' && col.field !== 'recipe_fooditem_id'
    })
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/recipes`)
  } catch (e) {
    console.error('Failed to fetch recipes', e)
  } finally {
    isLoading.value = false
  }
}

async function showMeals() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/meals')
    const list = data?.meals ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0]).filter(col => {
      return col.field !== 'fooditems' && col.field !== 'meal_recipe_id'
    })
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/meals`)
  } catch (e) {
    console.error('Failed to fetch meals', e)
  } finally {
    isLoading.value = false
  }
}

async function showFoodItems() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/food-items')
    const list = data?.food_items ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0]).filter(col => {
      return col.field !== 'recipe'
    })
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/fooditems`)
  } catch (e) {
    console.error('Failed to fetch food items', e)
  } finally {
    isLoading.value = false
  }
}

async function showUnitTypes() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/unit-types')
    const list = data?.unit_types ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0])
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/unittypes`)
  } catch (e) {
    console.error('Failed to fetch unit types', e)
  } finally {
    isLoading.value = false
  }
}

async function showCategories() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/categories')
    const list = data?.categories ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0])
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/categories`)
  } catch (e) {
    console.error('Failed to fetch categories', e)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <Header />
  <div class="flex pb-4">
    <MainMenu 
      class="min-h-screen"
      @showHome="showHome"
      @showRandomIngredient="showIngredients"
      @showRandomRecipe="showRecipes"
      @showRandomMeal="showMeals"
      @showRandomFoodItem="showFoodItems"
      @showUnitTypes="showUnitTypes"
      @showCategories="showCategories"
    />
    <router-view
      :itemData="itemData" />
    <div v-if="isLoading" class="loading-overlay">
      <div class="spinner"></div>
    </div>
  </div>
  <Footer class="fixed bottom-0 left-0 w-full" />
</template>

<style>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(255,255,255,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.spinner {
  width: 48px;
  height: 48px;
  border: 6px solid #ccc;
  border-top: 6px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
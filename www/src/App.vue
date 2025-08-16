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

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`)
  return res.json()
}

async function showHome() {
  try {
    const data = await fetchJSON('/recipes')
    const list = data?.recipes ?? []
    if (!Array.isArray(list)) return
    const columns = list.length ? getColumns(list[0]) : []
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/`)
  } catch (e) {
    console.error('Failed to load home list', e)
  }
}

async function showIngredients() {
  try {
    const data = await fetchJSON('/ingredients')
    const list = data?.ingredients ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = getColumns(list[0])
    itemData.value = {
      items: list,
      columns
    }
    router.push(`/ingredients`)
  } catch (e) {
    console.error('Failed to fetch ingredients', e)
  }
}

async function showRecipes() {
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
  }
}

async function showMeals() {
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
  }
}

async function showFoodItems() {
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
		/>
		<router-view
			:itemData="itemData" />
	</div>
	<Footer class="fixed bottom-0 left-0 w-full" />
</template>
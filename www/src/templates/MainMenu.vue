<template>
	<nav class="flex flex-col space-y-4 p-2 bg-gray-100 w-40 min-h-screen">
		<button @click="showHome">Home</button>
		<button @click="showIngredients">Ingredient Details</button>
		<button @click="showRecipes">Recipe Details</button>
		<button @click="showMeals">Meal Details</button>
		<button @click="showFoodItems">Food Item Details</button>
		<button @click="showUnitTypes">Unit Types</button>
		<button @click="showCategories">Categories</button>
	</nav>
</template>

<script setup>
import { useNavigation } from '../composables/useNavigation.js'

const emit = defineEmits(['updateItemData', 'updateLoading'])

const {
  router,
  itemData,
  isLoading,
  getColumns,
  removeColumns,
  parseItemData,
  fetchJSON
} = useNavigation()

// Watch for changes and emit to parent
import { watch } from 'vue'
watch(itemData, (newValue) => {
  emit('updateItemData', newValue)
}, { deep: true })

watch(isLoading, (newValue) => {
  emit('updateLoading', newValue)
})

async function showHome() {
  router.push('/')
}

async function showIngredients() {
  isLoading.value = true
  try {
    const data = await fetchJSON('/ingredients')
    const list = data?.ingredients ?? []
    if (!Array.isArray(list) || list.length === 0) return
    const columns = removeColumns(getColumns(list[0]), [
      'ingredient_description',
      'ingredient_notes',
      'created_at'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
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
    const columns = removeColumns(getColumns(list[0]), [
      'recipe_description',
      'ingredients',
      'instructions',
      'recipe_fooditem_id',
      'created_at'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
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
    const columns = removeColumns(getColumns(list[0]), [
      'fooditems',
      'meal_recipe_id',
      'created_at',
      'meal_description'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
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
    const columns = removeColumns(getColumns(list[0]), [
      'recipe',
      'created_at',
      'fooditem_description'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
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
    const columns = removeColumns(getColumns(list[0]), [
      'created_at'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
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
    const columns = removeColumns(getColumns(list[0]), [
      'created_at',
      'category_description',
      'parent_category_id'
    ])
    itemData.value = parseItemData({
      items: list,
      columns
    })
    router.push(`/categories`)
  } catch (e) {
    console.error('Failed to fetch categories', e)
  } finally {
    isLoading.value = false
  }
}
</script>
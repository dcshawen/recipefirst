<script setup>
import { ref } from 'vue'
import ingredients from './dev/ingredients.json'
import recipes from './dev/recipes.json'
import meals from './dev/meals.json'
import { useRouter, useRoute } from 'vue-router'

function getColumns(obj) {
  return Object.keys(obj).map(key => ({
    field: key,
    label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
  }))
}

const router = useRouter()
const itemData = ref({
	item: null,
	columns: []
})

function showRandomIngredient() {
  const item = ingredients[Math.floor(Math.random() * ingredients.length)]
  itemData.value = {
    item,
    columns: getColumns(item).slice(1) // Exclude the first column (name)
  }
  router.push('/ingredients/2')
}

function showRandomRecipe() {
  const item = recipes[Math.floor(Math.random() * recipes.length)]
  itemData.value = {
    item,
    columns: getColumns(item).slice(1) // Exclude the first column (name)
  }
  router.push('/recipes/2')
}

function showRandomMeal() {
  const item = meals[Math.floor(Math.random() * meals.length)]
  itemData.value = {
    item,
    columns: getColumns(item).slice(1) // Exclude the first column (name)
  }
  router.push('/meals/2')
}

</script>

<template>
	<nav class="flex space-x-4 p-2 bg-gray-100">
		<router-link to="/">Home</router-link>
		<button @click="showRandomIngredient">Ingredient Details</button>
		<button @click="showRandomRecipe">Recipe Details</button>
		<button @click="showRandomMeal">Meal Details</button>
	</nav>
	<router-view :itemData="itemData" />
</template>
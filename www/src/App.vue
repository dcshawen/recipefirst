<script setup>
import { ref } from 'vue'
import ingredients from './dev/ingredients.json'
import recipes from './dev/recipes.json'
import meals from './dev/meals.json'
import { useRouter, useRoute } from 'vue-router'
import Header from './templates/Header.vue'
import MainMenu from './templates/MainMenu.vue'
import Footer from './templates/Footer.vue'
import ItemDetails from './pages/ItemDetails.vue'
import router from './routes.js'

function getColumns(obj) {
  return Object.keys(obj).map(key => ({
    field: key,
    label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
  }))
}

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
	<Header />
	<div class="flex pb-4">
		<MainMenu 
			class="min-h-screen"
			@showRandomIngredient="showRandomIngredient"
			@showRandomRecipe="showRandomRecipe"
			@showRandomMeal="showRandomMeal"
		/>
		<router-view
			class="h-fit"
			:itemData="itemData" />
	</div>
	<Footer class="fixed bottom-0 left-0 w-full" />
</template>
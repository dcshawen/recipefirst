<script setup>
	import IngredientListView from './components/IngredientListView.vue'
	import { ref } from 'vue'

	let ingredients = ref([
		{ id: 1, name: 'Flour', description: "All-purpose flour", notes: "Follow recipe", created_at: new Date() },
		{ id: 2, name: 'Sugar', description: "Granulated sugar", notes: "Adjust to taste", created_at: new Date() },
		{ id: 3, name: 'Eggs', description: "Large eggs", notes: "Use fresh eggs", created_at: new Date() }
	])
</script>

<template>
	<IngredientListView :ingredients="ingredients" />
</template>

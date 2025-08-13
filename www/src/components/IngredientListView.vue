<template>
	<div class="ingredient-list-view">
		<IngredientListViewItem
			v-for="(ingredient, index) in ingredients"
			:key="ingredient.id || index"
			:ingredient="ingredient"
		/>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import IngredientListViewItem from './IngredientListViewItem.vue'

// Example ingredients data
const ingredients = ref([
	{ id: 1, name: 'Flour', amount: '2 cups' },
	{ id: 2, name: 'Sugar', amount: '1 cup' },
	{ id: 3, name: 'Eggs', amount: '3' }
])
</script>

<style scoped>
.ingredient-list-view {
	display: flex;
	flex-direction: column;
	gap: 8px;
}
</style>
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
import IngredientListViewItem from './IngredientListViewItem.vue'

defineProps({
	ingredients: {
		type: Array,
		required: true
	}
})
</script>

<style scoped>
.ingredient-list-view {
	display: flex;
	flex-direction: column;
	gap: 8px;
}
</style>
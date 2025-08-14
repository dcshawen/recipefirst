<template>
	<div class="ingredient-list-view">
		<div class="ingredient-list-header flex">
			<span
				v-for="(column, idx) in ingredientData.columns"
				:key="column.key || idx"
				class="ingredient-list-column"
			>
				{{ column.name }}
			</span>
		</div>
		<div
			v-for="(ingredient, index) in ingredientData.ingredients"
			:key="ingredient.id || index"
			class="ingredient-list-row flex"
		>
			<span
				v-for="(column, idx) in ingredientData.columns"
				:key="column.key || idx"
				class="ingredient-list-cell"
			>
				{{ ingredient[column.field] }}
			</span>
		</div>
	</div>
</template>

<script setup>
defineProps({
	ingredientData: {
		type: Object,
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
.ingredient-list-header,
.ingredient-list-row {
	display: flex;
}
.ingredient-list-column,
.ingredient-list-cell {
	flex: 1 1 0;
	padding: 0.5em;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}
.ingredient-list-header {
	font-weight: bold;
	background: #f9fafb;
	border-bottom: 1px solid #e5e7eb;
}
.ingredient-list-row {
	border-bottom: 1px solid #e5e7eb;
	align-items: center;
}
</style>
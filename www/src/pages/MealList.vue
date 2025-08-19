<template>
	<GenericList :config="mealConfig" />
</template>

<script setup>
import GenericList from '../components/GenericList.vue'

const mealConfig = {
	endpoint: '/meals',
	dataKey: 'meals',
	idField: 'meal_id',
	routePrefix: 'meals',
	columns: [
		{
			key: 'name',
			label: 'Meal Name',
			field: 'meal_name',
			type: 'link'
		},
		{
			key: 'updated',
			label: 'Last Updated',
			field: 'updated_at',
			type: 'date'
		}
	]
}
</script>

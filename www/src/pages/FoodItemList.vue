<template>
	<GenericList :config="foodItemConfig" />
</template>

<script setup>
import GenericList from '../components/GenericList.vue'

const foodItemConfig = {
	endpoint: '/food-items',
	dataKey: 'food_items',
	idField: 'fooditem_id',
	routePrefix: 'fooditems',
	columns: [
		{
			key: 'name',
			label: 'Food Item Name',
			field: 'fooditem_name',
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

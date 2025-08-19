<template>
	<GenericList :config="categoryConfig" />
</template>

<script setup>
import GenericList from '../components/GenericList.vue'

const categoryConfig = {
	endpoint: '/categories',
	dataKey: 'categories',
	idField: 'category_id',
	routePrefix: 'categories',
	columns: [
		{
			key: 'name',
			label: 'Category Name',
			field: 'category_name',
			type: 'text'
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

<template>
	<GenericList :config="unitTypeConfig" />
</template>

<script setup>
import GenericList from '../components/GenericList.vue'

const unitTypeConfig = {
	endpoint: '/unit-types',
	dataKey: 'unit_types',
	idField: 'id',
	routePrefix: 'unittypes',
	columns: [
		{
			key: 'type',
			label: 'Unit Type',
			field: 'unit_type',
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

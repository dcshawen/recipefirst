<template>
	<div>
		<GenericList :config="unitTypeConfig" />
		<v-btn
			color="primary"
			icon="mdi-plus"
			size="large"
			position="fixed"
			location="bottom right"
			class="mb-16 mr-4"
			@click="navigateToCreate"
		></v-btn>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import GenericList from '../components/GenericList.vue'

const router = useRouter()

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

const navigateToCreate = () => {
	router.push('/unittypes/create')
}
</script>

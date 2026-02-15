<template>
	<div>
		<GenericList :config="unitTypeConfig" />
		<button
			class="fixed bottom-20 right-4 w-14 h-14 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 flex items-center justify-center text-2xl transition-colors"
			@click="navigateToCreate"
		>
			<i class="mdi mdi-plus"></i>
		</button>
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

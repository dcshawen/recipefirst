<template>
	<div>
		<GenericList :config="foodItemConfig" />
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

const navigateToCreate = () => {
	router.push('/fooditems/create')
}
</script>

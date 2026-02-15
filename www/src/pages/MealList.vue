<template>
	<div>
		<GenericList :config="mealConfig" />
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

const navigateToCreate = () => {
	router.push('/meals/create')
}
</script>

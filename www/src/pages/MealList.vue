<template>
	<div>
		<GenericList :config="mealConfig" />
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

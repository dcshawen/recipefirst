<template>
	<div>
		<GenericList :config="foodItemConfig" />
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

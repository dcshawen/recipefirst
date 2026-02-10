<template>
	<div>
		<GenericList :config="categoryConfig" />
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

const navigateToCreate = () => {
	router.push('/categories/create')
}
</script>

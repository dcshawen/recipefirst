<template>
	<div>
		<GenericList :config="categoryConfig" />
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

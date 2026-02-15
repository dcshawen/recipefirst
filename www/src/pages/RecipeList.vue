<template>
	<div>
		<GenericList :config="recipeConfig" />
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

const recipeConfig = {
	endpoint: '/recipes',
	dataKey: 'recipes',
	idField: 'recipe_id',
	routePrefix: 'recipes',
	columns: [
		{
			key: 'name',
			label: 'Recipe Name',
			field: 'recipe_name',
			type: 'link'
		},
		{
			key: 'category',
			label: 'Category',
			field: 'categories',
			type: 'categories'
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
	router.push('/recipes/create')
}
</script>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(255,255,255,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.spinner {
  width: 48px;
  height: 48px;
  border: 6px solid #ccc;
  border-top: 6px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>

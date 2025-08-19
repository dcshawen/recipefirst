<template>
	<GenericList :config="ingredientConfig" />
</template>

<script setup>
import GenericList from '../components/GenericList.vue'

const ingredientConfig = {
	endpoint: '/ingredients',
	dataKey: 'ingredients',
	idField: 'ingredient_id',
	routePrefix: 'ingredients',
	columns: [
		{
			key: 'name',
			label: 'Ingredient',
			field: 'ingredient_name',
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
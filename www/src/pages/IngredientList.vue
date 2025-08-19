<template>
	<div class="p-4 w-full">
		<h1 class="text-2xl font-bold mb-4">Ingredients</h1>
		<div v-if="isLoading" class="loading-overlay">
			<div class="spinner"></div>
		</div>
		<v-table v-else theme="dark" class="w-full">
			<thead>
				<tr>
					<th>Ingredient</th>
					<th>Last Updated</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="ingredient in ingredients" :key="ingredient.ingredient_id">
					<td>
						<router-link :to="{ path: `/ingredients/${ingredient.ingredient_id}` }">
							{{ ingredient.ingredient_name }}
						</router-link>
					</td>
					<td>{{ new Date(ingredient.updated_at).toLocaleDateString() }}</td>
				</tr>
			</tbody>
		</v-table>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useNavigation } from '../composables/useNavigation.js'

const ingredients = ref([])
const isLoading = ref(false)
const { fetchJSON } = useNavigation()

async function fetchIngredients() {
	isLoading.value = true
	try {
		const data = await fetchJSON('/ingredients')
		ingredients.value = data?.ingredients ?? []
	} catch (error) {
		console.error('Failed to fetch ingredients:', error)
	} finally {
		isLoading.value = false
	}
}

onMounted(() => {
	fetchIngredients()
})
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
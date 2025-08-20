<template>
	<div class="p-4 w-full">
		<div v-if="isLoading" class="loading-overlay">
			<div class="spinner"></div>
		</div>
		<v-table v-else theme="light" class="w-full">
			<thead>
				<tr>
					<th
						v-for="column in columns" :key="column.key"
						class="text-h6 pa-2"
					>
						{{ column.label }}
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="item in items" :key="item[config.idField]">
					<td v-for="column in columns" :key="column.key" >
						<template v-if="column.type === 'link'">
							<router-link :to="{ path: `/${config.routePrefix}/${item[config.idField]}` }">
								{{ getFieldValue(item, column.field) }}
							</router-link>
						</template>
						<template v-else-if="column.type === 'date'">
							{{ new Date(getFieldValue(item, column.field)).toLocaleDateString() }}
						</template>
						<template v-else-if="column.type === 'categories'">
							<span v-if="item[column.field] && item[column.field].length > 0">
								{{ item[column.field].map(cat => cat.category_name || cat.name || cat).join(', ') }}
							</span>
							<span v-else class="text-gray-500"></span>
						</template>
						<template v-else>
							{{ getFieldValue(item, column.field) }}
						</template>
					</td>
				</tr>
			</tbody>
		</v-table>
	</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useNavigation } from '../composables/useNavigation.js'

const props = defineProps({
	config: {
		type: Object,
		required: true,
		validator: (config) => {
			return config.endpoint && config.dataKey && config.idField && config.routePrefix && config.columns
		}
	}
})

const items = ref([])
const isLoading = ref(false)
const { fetchJSON } = useNavigation()

const columns = computed(() => props.config.columns)

function getFieldValue(item, field) {
	return item[field] || ''
}

async function fetchData() {
	isLoading.value = true
	try {
		const data = await fetchJSON(props.config.endpoint)
		items.value = data?.[props.config.dataKey] ?? []
	} catch (error) {
		console.error(`Failed to fetch ${props.config.dataKey}:`, error)
	} finally {
		isLoading.value = false
	}
}

onMounted(() => {
	fetchData()
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

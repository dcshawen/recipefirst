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
						class="text-h6 pa-2 sortable-header"
						@click="toggleSort(column)"
					>
						<span class="header-content">
							{{ column.label }}
							<span class="sort-icon">
								<v-icon v-if="sortBy === column.field && sortOrder === 'asc'" size="small">mdi-arrow-up</v-icon>
								<v-icon v-else-if="sortBy === column.field && sortOrder === 'desc'" size="small">mdi-arrow-down</v-icon>
								<v-icon v-else size="small" class="sort-inactive">mdi-unfold-more-horizontal</v-icon>
							</span>
						</span>
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="item in pagedItems" :key="item[config.idField]">
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
		<div class="d-flex justify-center mt-4">
			<v-pagination
				v-model="page"
				:length="pageCount"
				:total-visible="4"
				color="primary"
				rounded
				show-first-last-page
				prev-icon="mdi-chevron-left"
				next-icon="mdi-chevron-right"
			/>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
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
const page = ref(1)
const itemsPerPage = ref(10)
const sortBy = ref(null)
const sortOrder = ref('asc')

const sortedItems = computed(() => {
	if (!sortBy.value) return items.value

	const sorted = [...items.value].sort((a, b) => {
		const aVal = getFieldValue(a, sortBy.value)
		const bVal = getFieldValue(b, sortBy.value)
		
		// Handle null/undefined values
		if (aVal === null || aVal === undefined || aVal === '') return 1
		if (bVal === null || bVal === undefined || bVal === '') return -1
		
		// Try to parse as numbers if possible
		const aNum = Number(aVal)
		const bNum = Number(bVal)
		
		if (!isNaN(aNum) && !isNaN(bNum)) {
			return sortOrder.value === 'asc' ? aNum - bNum : bNum - aNum
		}
		
		// Try to parse as dates
		const aDate = new Date(aVal)
		const bDate = new Date(bVal)
		if (!isNaN(aDate.getTime()) && !isNaN(bDate.getTime())) {
			return sortOrder.value === 'asc' ? aDate - bDate : bDate - aDate
		}
		
		// Default to string comparison
		const aStr = String(aVal).toLowerCase()
		const bStr = String(bVal).toLowerCase()
		
		if (sortOrder.value === 'asc') {
			return aStr.localeCompare(bStr)
		} else {
			return bStr.localeCompare(aStr)
		}
	})
	
	return sorted
})

const pageCount = computed(() => Math.ceil(sortedItems.value.length / itemsPerPage.value))
const pagedItems = computed(() => {
	const start = (page.value - 1) * itemsPerPage.value
	return sortedItems.value.slice(start, start + itemsPerPage.value)
})

function getFieldValue(item, field) {
	return item[field] || ''
}

function toggleSort(column) {
	if (sortBy.value === column.field) {
		// If already sorting by this column, toggle the order
		sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
	} else {
		// New column, default to ascending
		sortBy.value = column.field
		sortOrder.value = 'asc'
	}
	// Reset to first page when sorting changes
	page.value = 1
}

async function fetchData() {
	isLoading.value = true
	try {
		const data = await fetchJSON(props.config.endpoint)
		items.value = data?.[props.config.dataKey] ?? []
		page.value = 1 // Reset to first page on new data
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

.sortable-header {
  cursor: pointer;
  user-select: none;
  transition: background-color 0.2s;
}

.sortable-header:hover {
  background-color: rgba(0, 0, 0, 0.04);
}

.header-content {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.sort-icon {
  display: inline-flex;
  align-items: center;
}

.sort-inactive {
  opacity: 0.3;
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

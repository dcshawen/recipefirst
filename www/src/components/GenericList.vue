<template>
	<div class="p-4 w-full">
		<div v-if="isLoading" class="loading-overlay">
			<div class="spinner"></div>
		</div>
		<table v-else class="w-full bg-white border-collapse">
			<thead>
				<tr class="border-b border-gray-200">
					<th
						v-for="column in columns" :key="column.key"
						class="text-left text-sm font-semibold text-gray-700 px-4 py-3 cursor-pointer select-none hover:bg-gray-50 transition-colors"
						@click="toggleSort(column)"
					>
						<span class="inline-flex items-center gap-1">
							{{ column.label }}
							<i v-if="sortBy === column.field && sortOrder === 'asc'" class="mdi mdi-arrow-up text-sm"></i>
							<i v-else-if="sortBy === column.field && sortOrder === 'desc'" class="mdi mdi-arrow-down text-sm"></i>
							<i v-else class="mdi mdi-unfold-more-horizontal text-sm opacity-30"></i>
						</span>
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="item in pagedItems" :key="item[config.idField]" class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
					<td v-for="column in columns" :key="column.key" class="px-4 py-3 text-sm">
						<template v-if="column.type === 'link'">
							<router-link
								:to="{ path: `/${config.routePrefix}/${item[config.idField]}` }"
								class="text-blue-600 hover:text-blue-800 hover:underline"
							>
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
		</table>
		<!-- Pagination -->
		<div v-if="pageCount > 1" class="flex justify-center items-center gap-1 mt-4">
			<button
				class="px-2 py-1 rounded text-sm hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
				:disabled="page === 1"
				@click="page = 1"
			>
				<i class="mdi mdi-chevron-double-left"></i>
			</button>
			<button
				class="px-2 py-1 rounded text-sm hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
				:disabled="page === 1"
				@click="page = page - 1"
			>
				<i class="mdi mdi-chevron-left"></i>
			</button>
			<button
				v-for="p in visiblePages"
				:key="p"
				class="w-8 h-8 rounded text-sm transition-colors"
				:class="p === page ? 'bg-blue-600 text-white' : 'hover:bg-gray-100 text-gray-700'"
				@click="page = p"
			>
				{{ p }}
			</button>
			<button
				class="px-2 py-1 rounded text-sm hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
				:disabled="page === pageCount"
				@click="page = page + 1"
			>
				<i class="mdi mdi-chevron-right"></i>
			</button>
			<button
				class="px-2 py-1 rounded text-sm hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
				:disabled="page === pageCount"
				@click="page = pageCount"
			>
				<i class="mdi mdi-chevron-double-right"></i>
			</button>
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

const visiblePages = computed(() => {
	const total = pageCount.value
	const current = page.value
	const maxVisible = 5
	let start = Math.max(1, current - Math.floor(maxVisible / 2))
	let end = Math.min(total, start + maxVisible - 1)
	if (end - start + 1 < maxVisible) {
		start = Math.max(1, end - maxVisible + 1)
	}
	const pages = []
	for (let i = start; i <= end; i++) {
		pages.push(i)
	}
	return pages
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

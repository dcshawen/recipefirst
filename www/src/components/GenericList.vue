<template>
	<div class="page-container">
		<div v-if="isLoading" class="loading-overlay">
			<div class="spinner"></div>
		</div>

		<div v-else-if="pagedItems.length === 0" class="empty-state">
			<i class="mdi mdi-magnify"></i>
			<p class="text-sm">No items found.</p>
		</div>

		<div v-else class="card overflow-hidden">
			<table class="data-table">
				<thead>
					<tr>
						<th
							v-for="column in columns" :key="column.key"
							@click="toggleSort(column)"
						>
							<span class="inline-flex items-center gap-1">
								{{ column.label }}
								<i v-if="sortBy === column.field && sortOrder === 'asc'" class="mdi mdi-arrow-up text-xs"></i>
								<i v-else-if="sortBy === column.field && sortOrder === 'desc'" class="mdi mdi-arrow-down text-xs"></i>
								<i v-else class="mdi mdi-unfold-more-horizontal text-xs opacity-30"></i>
							</span>
						</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="item in pagedItems" :key="item[config.idField]">
						<td v-for="column in columns" :key="column.key">
							<template v-if="column.type === 'link'">
								<router-link
									:to="{ path: `/${config.routePrefix}/${item[config.idField]}` }"
									class="text-brand-600 hover:text-brand-800 font-medium hover:underline"
								>
									{{ getFieldValue(item, column.field) }}
								</router-link>
							</template>
							<template v-else-if="column.type === 'date'">
								<span class="text-gray-500">{{ new Date(getFieldValue(item, column.field)).toLocaleDateString() }}</span>
							</template>
							<template v-else-if="column.type === 'categories'">
								<span v-if="item[column.field] && item[column.field].length > 0" class="flex flex-wrap gap-1">
									<span v-for="cat in item[column.field]" :key="cat.category_name || cat" class="chip">{{ cat.category_name || cat.name || cat }}</span>
								</span>
								<span v-else class="text-gray-400">&mdash;</span>
							</template>
							<template v-else>
								{{ getFieldValue(item, column.field) }}
							</template>
						</td>
					</tr>
				</tbody>
			</table>
		</div>

		<!-- Pagination -->
		<div v-if="pageCount > 1" class="pagination">
			<button class="page-btn" :disabled="page === 1" @click="page = 1">
				<i class="mdi mdi-chevron-double-left"></i>
			</button>
			<button class="page-btn" :disabled="page === 1" @click="page = page - 1">
				<i class="mdi mdi-chevron-left"></i>
			</button>
			<button
				v-for="p in visiblePages"
				:key="p"
				class="page-btn"
				:class="{ 'is-active': p === page }"
				@click="page = p"
			>
				{{ p }}
			</button>
			<button class="page-btn" :disabled="page === pageCount" @click="page = page + 1">
				<i class="mdi mdi-chevron-right"></i>
			</button>
			<button class="page-btn" :disabled="page === pageCount" @click="page = pageCount">
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



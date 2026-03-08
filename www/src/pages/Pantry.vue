<template>
  <div class="w-[92vw] sm:w-[50vw] mx-auto mt-8">
    <div class="relative pt-4 sm:pt-16">

      <!-- Desktop Add New button -->
      <button
        class="absolute top-4 right-4 z-10 hidden sm:flex items-center gap-2 bg-blue-600 text-white px-3 py-2 rounded-md shadow hover:bg-blue-700 transition-colors text-sm"
        @click="router.push('/ingredients/create')"
      >
        <i class="mdi mdi-plus"></i>
        <span>Add Ingredient</span>
      </button>

      <!-- Loading -->
      <div v-if="isLoading" class="loading-overlay">
        <div class="spinner"></div>
      </div>

      <!-- Empty -->
      <div v-else-if="pagedItems.length === 0" class="empty-state">
        <i class="mdi mdi-magnify"></i>
        <p class="text-sm">No items found.</p>
      </div>

      <!-- Table -->
      <div v-else class="card overflow-hidden">
        <table class="data-table">
          <thead>
            <tr>
              <th @click="toggleSort('name')" class="cursor-pointer select-none">
                <span class="inline-flex items-center gap-1">
                  Name
                  <i v-if="sortBy === 'name' && sortOrder === 'asc'" class="mdi mdi-arrow-up text-xs"></i>
                  <i v-else-if="sortBy === 'name' && sortOrder === 'desc'" class="mdi mdi-arrow-down text-xs"></i>
                  <i v-else class="mdi mdi-unfold-more-horizontal text-xs opacity-30"></i>
                </span>
              </th>
              <th @click="toggleSort('type')" class="cursor-pointer select-none">
                <span class="inline-flex items-center gap-1">
                  Type
                  <i v-if="sortBy === 'type' && sortOrder === 'asc'" class="mdi mdi-arrow-up text-xs"></i>
                  <i v-else-if="sortBy === 'type' && sortOrder === 'desc'" class="mdi mdi-arrow-down text-xs"></i>
                  <i v-else class="mdi mdi-unfold-more-horizontal text-xs opacity-30"></i>
                </span>
              </th>
              <th @click="toggleSort('updated_at')" class="cursor-pointer select-none">
                <span class="inline-flex items-center gap-1">
                  Last Updated
                  <i v-if="sortBy === 'updated_at' && sortOrder === 'asc'" class="mdi mdi-arrow-up text-xs"></i>
                  <i v-else-if="sortBy === 'updated_at' && sortOrder === 'desc'" class="mdi mdi-arrow-down text-xs"></i>
                  <i v-else class="mdi mdi-unfold-more-horizontal text-xs opacity-30"></i>
                </span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in pagedItems" :key="item._key">
              <td>
                <router-link
                  :to="item._route"
                  class="text-brand-600 hover:text-brand-800 font-medium hover:underline"
                >
                  {{ item.name }}
                </router-link>
              </td>
              <td>
                <span class="chip">{{ item.type }}</span>
              </td>
              <td>
                <span class="text-gray-500">{{ new Date(item.updated_at).toLocaleDateString() }}</span>
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
        <button class="page-btn" :disabled="page === 1" @click="page--">
          <i class="mdi mdi-chevron-left"></i>
        </button>
        <button
          v-for="p in visiblePages"
          :key="p"
          class="page-btn"
          :class="{ 'is-active': p === page }"
          @click="page = p"
        >{{ p }}</button>
        <button class="page-btn" :disabled="page === pageCount" @click="page++">
          <i class="mdi mdi-chevron-right"></i>
        </button>
        <button class="page-btn" :disabled="page === pageCount" @click="page = pageCount">
          <i class="mdi mdi-chevron-double-right"></i>
        </button>
      </div>
    </div>

    <!-- Mobile FAB -->
    <button
      class="fixed bottom-20 right-4 w-14 h-14 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 flex items-center justify-center text-2xl transition-colors sm:hidden"
      title="Add Ingredient"
      @click="router.push('/ingredients/create')"
    >
      <i class="mdi mdi-plus" />
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNavigation } from '../composables/useNavigation.js'

const router = useRouter()
const { fetchJSON } = useNavigation()

const isLoading = ref(false)
const allItems = ref([])
const page = ref(1)
const itemsPerPage = 10
const sortBy = ref('name')
const sortOrder = ref('asc')

async function fetchData() {
  isLoading.value = true
  try {
    const [fiData, ingData] = await Promise.all([
      fetchJSON('/food-items'),
      fetchJSON('/ingredients')
    ])
    const foodItems = (fiData?.food_items ?? []).map(fi => ({
      _key: `fi-${fi.fooditem_id}`,
      _route: `/fooditems/${fi.fooditem_id}`,
      name: fi.fooditem_name,
      type: 'Food Item',
      updated_at: fi.updated_at
    }))
    const ingredients = (ingData?.ingredients ?? []).map(ing => ({
      _key: `ing-${ing.ingredient_id}`,
      _route: `/ingredients/${ing.ingredient_id}`,
      name: ing.ingredient_name,
      type: 'Ingredient',
      updated_at: ing.updated_at
    }))
    allItems.value = [...foodItems, ...ingredients]
    page.value = 1
  } catch (err) {
    console.error('Failed to fetch pantry data:', err)
  } finally {
    isLoading.value = false
  }
}

const sortedItems = computed(() => {
  const field = sortBy.value
  return [...allItems.value].sort((a, b) => {
    const aVal = a[field] ?? ''
    const bVal = b[field] ?? ''
    const aDate = new Date(aVal)
    const bDate = new Date(bVal)
    const isDate = !isNaN(aDate.getTime()) && !isNaN(bDate.getTime()) && field === 'updated_at'
    let cmp
    if (isDate) {
      cmp = aDate - bDate
    } else {
      cmp = String(aVal).toLowerCase().localeCompare(String(bVal).toLowerCase())
    }
    return sortOrder.value === 'asc' ? cmp : -cmp
  })
})

const pageCount = computed(() => Math.ceil(sortedItems.value.length / itemsPerPage))
const pagedItems = computed(() => {
  const start = (page.value - 1) * itemsPerPage
  return sortedItems.value.slice(start, start + itemsPerPage)
})
const visiblePages = computed(() => {
  const total = pageCount.value
  const current = page.value
  const maxVisible = 5
  let start = Math.max(1, current - Math.floor(maxVisible / 2))
  let end = Math.min(total, start + maxVisible - 1)
  if (end - start + 1 < maxVisible) start = Math.max(1, end - maxVisible + 1)
  const pages = []
  for (let i = start; i <= end; i++) pages.push(i)
  return pages
})

function toggleSort(field) {
  if (sortBy.value === field) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = field
    sortOrder.value = 'asc'
  }
  page.value = 1
}

onMounted(fetchData)
</script>

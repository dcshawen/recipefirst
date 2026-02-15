<template>
  <div class="mx-auto max-w-[800px] bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Category</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Category Name *</label>
          <input
            v-model="formData.category_name"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.category_name ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.category_name" class="mt-1 text-xs text-red-600">{{ errors.category_name }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">e.g., Breakfast, Vegetarian, Italian</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea
            v-model="formData.category_description"
            rows="2"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
        </div>

        <!-- Parent Category Autocomplete -->
        <div class="mb-4 relative" ref="parentDropdownRef">
          <label class="block text-sm font-medium text-gray-700 mb-1">Parent Category</label>
          <div class="relative">
            <input
              v-model="parentSearch"
              type="text"
              class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Search categories..."
              @focus="parentDropdownOpen = true"
              @input="parentDropdownOpen = true"
            />
            <button
              v-if="formData.parent_category_id"
              type="button"
              class="absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
              @click="clearParentCategory"
            >
              <i class="mdi mdi-close text-sm"></i>
            </button>
          </div>
          <div v-if="parentDropdownOpen && filteredCategories.length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
            <button
              v-for="cat in filteredCategories"
              :key="cat.category_id"
              type="button"
              class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
              :class="formData.parent_category_id === cat.category_id ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
              @click="selectParentCategory(cat)"
            >
              {{ cat.category_name }}
            </button>
          </div>
          <div v-if="parentDropdownOpen && filteredCategories.length === 0 && parentSearch" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg p-3 text-sm text-gray-500">
            No categories found
          </div>
          <p class="mt-1 text-xs text-gray-500">Optional: Select a parent category for hierarchy</p>
        </div>
      </form>
    </div>

    <hr class="border-gray-200" />

    <div class="flex justify-between items-center px-6 py-4">
      <button
        type="button"
        class="px-4 py-2 text-sm text-gray-600 hover:text-gray-800 transition-colors"
        :disabled="loading"
        @click="$emit('cancel')"
      >
        Cancel
      </button>
      <button
        type="button"
        class="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm disabled:opacity-50"
        :disabled="loading"
        @click="handleSubmit"
      >
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Category' }}
      </button>
    </div>

    <div v-if="error" class="mx-4 mb-4 p-3 bg-red-50 border border-red-200 rounded-md flex justify-between items-center">
      <span class="text-sm text-red-700">{{ error }}</span>
      <button @click="error = null" class="text-red-400 hover:text-red-600"><i class="mdi mdi-close"></i></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch, computed } from 'vue'

const props = defineProps({
  loading: Boolean,
  error: String,
  initialData: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isEditMode = computed(() => !!props.initialData)

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

const errors = ref({})
const formData = ref({
  category_name: props.initialData?.category_name || '',
  category_description: props.initialData?.category_description || '',
  parent_category_id: props.initialData?.parent_category_id || null
})

const categories = ref([])
const loadingCategories = ref(false)

// Parent category autocomplete
const parentDropdownRef = ref(null)
const parentDropdownOpen = ref(false)
const parentSearch = ref('')

const filteredCategories = computed(() => {
  const q = parentSearch.value.toLowerCase()
  return categories.value.filter(c => c.category_name.toLowerCase().includes(q))
})

function selectParentCategory(cat) {
  formData.value.parent_category_id = cat.category_id
  parentSearch.value = cat.category_name
  parentDropdownOpen.value = false
}

function clearParentCategory() {
  formData.value.parent_category_id = null
  parentSearch.value = ''
}

// Click outside handler
function handleClickOutside(e) {
  if (parentDropdownRef.value && !parentDropdownRef.value.contains(e.target)) {
    parentDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  loadCategories()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Watch for initialData changes
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      category_name: newData.category_name || '',
      category_description: newData.category_description || '',
      parent_category_id: newData.parent_category_id || null
    }
    // Set parent search text from loaded categories
    if (newData.parent_category_id) {
      const parent = categories.value.find(c => c.category_id === newData.parent_category_id)
      if (parent) parentSearch.value = parent.category_name
    }
  }
}, { immediate: true })

// Also update parent search text once categories load
watch(categories, () => {
  if (formData.value.parent_category_id) {
    const parent = categories.value.find(c => c.category_id === formData.value.parent_category_id)
    if (parent) parentSearch.value = parent.category_name
  }
})

const loadCategories = async () => {
  loadingCategories.value = true
  try {
    const response = await fetch(`${API_BASE}/categories`)
    const data = await response.json()
    categories.value = data.categories || []
  } catch (err) {
    console.error('Failed to load categories:', err)
  } finally {
    loadingCategories.value = false
  }
}

function validate() {
  errors.value = {}
  if (!formData.value.category_name) {
    errors.value.category_name = 'Name is required'
  }
  return Object.keys(errors.value).length === 0
}

const handleSubmit = async () => {
  if (validate()) {
    emit('submit', formData.value)
  }
}
</script>

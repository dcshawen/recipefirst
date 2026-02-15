<template>
  <div class="mx-auto w-full bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Meal</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <form @submit.prevent="handleSubmit">
        <!-- Basic Information -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Meal Name *</label>
          <input
            v-model="formData.meal_name"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.meal_name ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.meal_name" class="mt-1 text-xs text-red-600">{{ errors.meal_name }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">e.g., Sunday Dinner, Weekday Lunch</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea
            v-model="formData.meal_description"
            rows="3"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
        </div>

        <hr class="border-gray-200 my-6" />

        <!-- Food Items Selection -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Food Items *</h3>
        <p v-if="errors.fooditems" class="mb-2 text-xs text-red-600">{{ errors.fooditems }}</p>

        <div v-for="(item, index) in selectedFoodItems" :key="index" class="mb-4 p-4 bg-gray-50 rounded-md">
          <div class="flex items-center gap-2">
            <div class="flex-1 relative" :ref="el => foodItemDropdownRefs[index] = el">
              <input
                v-model="foodItemSearches[index]"
                type="text"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Search food items..."
                @focus="openFoodItemDropdown(index)"
                @input="openFoodItemDropdown(index)"
              />
              <div v-if="foodItemDropdownOpenIndex === index && filteredFoodItems(index).length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
                <button
                  v-for="fi in filteredFoodItems(index)"
                  :key="fi.fooditem_id"
                  type="button"
                  class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
                  :class="item.fooditem_id === fi.fooditem_id ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
                  @click="selectFoodItemForRow(index, fi)"
                >
                  {{ fi.fooditem_name }}
                </button>
              </div>
              <div v-if="foodItemDropdownOpenIndex === index && filteredFoodItems(index).length === 0 && foodItemSearches[index]" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg p-3 text-sm text-gray-500">
                No food items found
              </div>
            </div>
            <button
              type="button"
              class="p-2 text-red-500 hover:text-red-700 transition-colors disabled:opacity-30"
              :disabled="selectedFoodItems.length === 1"
              @click="removeFoodItem(index)"
            >
              <i class="mdi mdi-delete text-lg"></i>
            </button>
          </div>
        </div>

        <button
          type="button"
          class="mb-6 px-4 py-2 border border-blue-600 text-blue-600 rounded-md text-sm font-medium hover:bg-blue-50 transition-colors inline-flex items-center gap-1"
          @click="addFoodItem"
        >
          <i class="mdi mdi-plus"></i> Add Food Item
        </button>

        <hr class="border-gray-200 my-6" />

        <!-- Categories Selection (Multi-select with chips) -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Categories (Optional)</h3>
        <div class="mb-4 relative" ref="categoryDropdownRef">
          <!-- Selected chips -->
          <div v-if="formData.category_ids.length > 0" class="flex flex-wrap gap-1 mb-2">
            <span
              v-for="catId in formData.category_ids"
              :key="catId"
              class="inline-flex items-center gap-1 px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full"
            >
              {{ getCategoryName(catId) }}
              <button type="button" class="hover:text-blue-600" @click="removeCategory(catId)">
                <i class="mdi mdi-close text-xs"></i>
              </button>
            </span>
          </div>
          <input
            v-model="categorySearch"
            type="text"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Search categories..."
            @focus="categoryDropdownOpen = true"
            @input="categoryDropdownOpen = true"
          />
          <div v-if="categoryDropdownOpen && filteredCategoriesForSelect.length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
            <button
              v-for="cat in filteredCategoriesForSelect"
              :key="cat.category_id"
              type="button"
              class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
              :class="formData.category_ids.includes(cat.category_id) ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
              @click="toggleCategory(cat.category_id)"
            >
              {{ cat.category_name }}
            </button>
          </div>
          <p class="mt-1 text-xs text-gray-500">Optional: Select one or more categories</p>
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
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Meal' }}
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
  meal_name: props.initialData?.meal_name || '',
  meal_description: props.initialData?.meal_description || '',
  category_ids: props.initialData?.category_ids || []
})

// Initialize selectedFoodItems from initialData if available
const initializeSelectedFoodItems = () => {
  if (props.initialData?.fooditems && Array.isArray(props.initialData.fooditems)) {
    return props.initialData.fooditems.map(item => ({
      fooditem_id: item.fooditem_id
    }))
  } else if (props.initialData?.fooditem_ids && Array.isArray(props.initialData.fooditem_ids)) {
    return props.initialData.fooditem_ids.map(id => ({ fooditem_id: id }))
  }
  return [{ fooditem_id: null }]
}

const selectedFoodItems = ref(initializeSelectedFoodItems())

const foodItems = ref([])
const categories = ref([])
const loadingFoodItems = ref(false)
const loadingCategories = ref(false)

// Food item autocomplete state
const foodItemSearches = ref([])
const foodItemDropdownRefs = ref([])
const foodItemDropdownOpenIndex = ref(null)

// Category multi-select autocomplete state
const categoryDropdownRef = ref(null)
const categoryDropdownOpen = ref(false)
const categorySearch = ref('')

// Initialize food item search texts
function initFoodItemSearchTexts() {
  foodItemSearches.value = selectedFoodItems.value.map(item => {
    if (item.fooditem_id) {
      const fi = foodItems.value.find(f => f.fooditem_id === item.fooditem_id)
      return fi ? fi.fooditem_name : ''
    }
    return ''
  })
}

function openFoodItemDropdown(index) {
  foodItemDropdownOpenIndex.value = index
}

function filteredFoodItems(index) {
  const q = (foodItemSearches.value[index] || '').toLowerCase()
  return foodItems.value.filter(f => f.fooditem_name.toLowerCase().includes(q))
}

function selectFoodItemForRow(index, fi) {
  selectedFoodItems.value[index].fooditem_id = fi.fooditem_id
  foodItemSearches.value[index] = fi.fooditem_name
  foodItemDropdownOpenIndex.value = null
}

const filteredCategoriesForSelect = computed(() => {
  const q = categorySearch.value.toLowerCase()
  return categories.value.filter(c => c.category_name.toLowerCase().includes(q))
})

function getCategoryName(catId) {
  const cat = categories.value.find(c => c.category_id === catId)
  return cat ? cat.category_name : catId
}

function toggleCategory(catId) {
  const idx = formData.value.category_ids.indexOf(catId)
  if (idx >= 0) {
    formData.value.category_ids.splice(idx, 1)
  } else {
    formData.value.category_ids.push(catId)
  }
}

function removeCategory(catId) {
  const idx = formData.value.category_ids.indexOf(catId)
  if (idx >= 0) formData.value.category_ids.splice(idx, 1)
}

// Click outside handler
function handleClickOutside(e) {
  // Close food item dropdowns
  if (foodItemDropdownOpenIndex.value !== null) {
    const ref = foodItemDropdownRefs.value[foodItemDropdownOpenIndex.value]
    if (ref && !ref.contains(e.target)) {
      foodItemDropdownOpenIndex.value = null
    }
  }
  // Close category dropdown
  if (categoryDropdownRef.value && !categoryDropdownRef.value.contains(e.target)) {
    categoryDropdownOpen.value = false
  }
}

// Watch for initialData changes (handles async loading)
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      meal_name: newData.meal_name || '',
      meal_description: newData.meal_description || '',
      category_ids: newData.category_ids || []
    }

    if (newData.fooditems && Array.isArray(newData.fooditems)) {
      selectedFoodItems.value = newData.fooditems.map(item => ({
        fooditem_id: item.fooditem_id
      }))
    } else if (newData.fooditem_ids && Array.isArray(newData.fooditem_ids)) {
      selectedFoodItems.value = newData.fooditem_ids.map(id => ({ fooditem_id: id }))
    }
    initFoodItemSearchTexts()
  }
}, { immediate: true })

// Update search texts when food items load
watch(foodItems, () => {
  initFoodItemSearchTexts()
})

const loadFoodItems = async () => {
  loadingFoodItems.value = true
  try {
    const response = await fetch(`${API_BASE}/food-items`)
    const data = await response.json()
    foodItems.value = data.food_items || []
  } catch (err) {
    console.error('Failed to load food items:', err)
  } finally {
    loadingFoodItems.value = false
  }
}

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

const addFoodItem = () => {
  selectedFoodItems.value.push({ fooditem_id: null })
  foodItemSearches.value.push('')
}

const removeFoodItem = (index) => {
  if (selectedFoodItems.value.length > 1) {
    selectedFoodItems.value.splice(index, 1)
    foodItemSearches.value.splice(index, 1)
  }
}

function validate() {
  errors.value = {}
  if (!formData.value.meal_name) {
    errors.value.meal_name = 'Meal name is required'
  }
  const fooditem_ids = selectedFoodItems.value.map(item => item.fooditem_id).filter(id => id !== null)
  if (fooditem_ids.length === 0) {
    errors.value.fooditems = 'Please select at least one food item'
  }
  return Object.keys(errors.value).length === 0
}

const handleSubmit = async () => {
  if (validate()) {
    const fooditem_ids = selectedFoodItems.value.map(item => item.fooditem_id).filter(id => id !== null)
    const submitData = {
      ...formData.value,
      fooditem_ids
    }
    emit('submit', submitData)
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  loadFoodItems()
  loadCategories()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

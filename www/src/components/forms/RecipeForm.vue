<template>
  <div class="mx-auto max-w-[1000px] bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Recipe</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <form @submit.prevent="handleSubmit">
        <!-- Basic Information -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Basic Information</h3>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Recipe Name *</label>
          <input
            v-model="formData.name"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.name ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.name" class="mt-1 text-xs text-red-600">{{ errors.name }}</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea
            v-model="formData.description"
            rows="3"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
        </div>

        <!-- Produces Food Item Autocomplete -->
        <div class="mb-4 relative" ref="foodItemDropdownRef">
          <label class="block text-sm font-medium text-gray-700 mb-1">Produces Food Item *</label>
          <input
            v-model="foodItemSearch"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.fooditem_id ? 'border-red-500' : 'border-gray-300'"
            placeholder="Search food items..."
            @focus="foodItemDropdownOpen = true"
            @input="foodItemDropdownOpen = true"
          />
          <div v-if="foodItemDropdownOpen" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
            <button
              v-for="fi in filteredFoodItemsForRecipe"
              :key="fi.fooditem_id"
              type="button"
              class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
              :class="formData.fooditem_id === fi.fooditem_id ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
              @click="selectProducesFoodItem(fi)"
            >
              {{ fi.fooditem_name }}
            </button>
            <div v-if="filteredFoodItemsForRecipe.length === 0 && foodItemSearch" class="px-3 py-2 text-sm text-gray-500">No food items found</div>
            <hr class="border-gray-200" />
            <button
              type="button"
              class="w-full text-left px-3 py-2 text-sm text-blue-600 hover:bg-blue-50 transition-colors font-medium"
              @click="showCreateFoodItemDialog = true; foodItemDropdownOpen = false"
            >
              <i class="mdi mdi-plus"></i> Create New Food Item
            </button>
          </div>
          <p v-if="errors.fooditem_id" class="mt-1 text-xs text-red-600">{{ errors.fooditem_id }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">Select the food item this recipe produces</p>
        </div>

        <hr class="border-gray-200 my-6" />

        <!-- Ingredients Section -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Ingredients *</h3>
        <p v-if="errors.ingredients" class="mb-2 text-xs text-red-600">{{ errors.ingredients }}</p>

        <div v-for="(ingredient, index) in ingredients" :key="index" class="mb-4 p-4 bg-gray-50 rounded-md">
          <div class="grid grid-cols-12 gap-2 items-start">
            <!-- Ingredient source autocomplete -->
            <div class="col-span-12 md:col-span-5 relative" :ref="el => ingredientDropdownRefs[index] = el">
              <label class="block text-xs font-medium text-gray-600 mb-1">Ingredient or Food Item *</label>
              <input
                v-model="ingredientSearches[index]"
                type="text"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Search..."
                @focus="ingredientDropdownOpenIndex = index"
                @input="ingredientDropdownOpenIndex = index"
              />
              <div v-if="ingredientDropdownOpenIndex === index" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
                <button
                  v-for="src in filteredIngredientSources(index)"
                  :key="src.id"
                  type="button"
                  class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
                  :class="ingredient.source?.id === src.id ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
                  @click="selectIngredientSource(index, src)"
                >
                  {{ src.name }}
                </button>
                <div v-if="filteredIngredientSources(index).length === 0 && ingredientSearches[index]" class="px-3 py-2 text-sm text-gray-500">No results</div>
                <hr class="border-gray-200" />
                <button
                  type="button"
                  class="w-full text-left px-3 py-2 text-sm text-blue-600 hover:bg-blue-50 transition-colors font-medium"
                  @click="openCreateIngredientDialog(index)"
                >
                  <i class="mdi mdi-plus"></i> Create New Ingredient
                </button>
              </div>
            </div>
            <!-- Quantity -->
            <div class="col-span-12 md:col-span-3">
              <label class="block text-xs font-medium text-gray-600 mb-1">Quantity *</label>
              <input
                v-model.number="ingredient.ri_quantity"
                type="number"
                step="0.25"
                min="0"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <!-- Unit type select -->
            <div class="col-span-12 md:col-span-3">
              <label class="block text-xs font-medium text-gray-600 mb-1">Unit *</label>
              <select
                v-model="ingredient.ri_unit_type_id"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
              >
                <option :value="null" disabled>Select unit...</option>
                <option v-for="ut in unitTypes" :key="ut.id" :value="ut.id">{{ ut.unit_type }}</option>
              </select>
            </div>
            <!-- Delete button -->
            <div class="col-span-12 md:col-span-1 flex items-end pb-1">
              <button
                type="button"
                class="p-2 text-red-500 hover:text-red-700 transition-colors disabled:opacity-30"
                :disabled="ingredients.length === 1"
                @click="removeIngredient(index)"
              >
                <i class="mdi mdi-delete text-lg"></i>
              </button>
            </div>
          </div>
        </div>

        <button
          type="button"
          class="mb-6 px-4 py-2 border border-blue-600 text-blue-600 rounded-md text-sm font-medium hover:bg-blue-50 transition-colors inline-flex items-center gap-1"
          @click="addIngredient"
        >
          <i class="mdi mdi-plus"></i> Add Ingredient
        </button>

        <hr class="border-gray-200 my-6" />

        <!-- Instructions Section -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Instructions *</h3>
        <p v-if="errors.instructions" class="mb-2 text-xs text-red-600">{{ errors.instructions }}</p>

        <div v-for="(instruction, index) in instructions" :key="index" class="mb-4">
          <div class="flex items-start gap-2">
            <div class="flex-1">
              <label class="block text-xs font-medium text-gray-600 mb-1">Step {{ index + 1 }} *</label>
              <textarea
                v-model="instruction.instruction_text"
                rows="2"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              ></textarea>
            </div>
            <button
              type="button"
              class="mt-6 p-2 text-red-500 hover:text-red-700 transition-colors disabled:opacity-30"
              :disabled="instructions.length === 1"
              @click="removeInstruction(index)"
            >
              <i class="mdi mdi-delete text-lg"></i>
            </button>
          </div>
        </div>

        <button
          type="button"
          class="mb-6 px-4 py-2 border border-blue-600 text-blue-600 rounded-md text-sm font-medium hover:bg-blue-50 transition-colors inline-flex items-center gap-1"
          @click="addInstruction"
        >
          <i class="mdi mdi-plus"></i> Add Step
        </button>

        <hr class="border-gray-200 my-6" />

        <!-- Categories Selection -->
        <h3 class="text-lg font-semibold text-gray-900 mb-3">Categories (Optional)</h3>
        <div class="mb-4 relative" ref="recipeCategoryDropdownRef">
          <div v-if="formData.category_ids.length > 0" class="flex flex-wrap gap-1 mb-2">
            <span
              v-for="catId in formData.category_ids"
              :key="catId"
              class="inline-flex items-center gap-1 px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full"
            >
              {{ getRecipeCategoryName(catId) }}
              <button type="button" class="hover:text-blue-600" @click="removeRecipeCategory(catId)">
                <i class="mdi mdi-close text-xs"></i>
              </button>
            </span>
          </div>
          <input
            v-model="recipeCategorySearch"
            type="text"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Search categories..."
            @focus="recipeCategoryDropdownOpen = true"
            @input="recipeCategoryDropdownOpen = true"
          />
          <div v-if="recipeCategoryDropdownOpen && filteredRecipeCategories.length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto">
            <button
              v-for="cat in filteredRecipeCategories"
              :key="cat.category_id"
              type="button"
              class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
              :class="formData.category_ids.includes(cat.category_id) ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
              @click="toggleRecipeCategory(cat.category_id)"
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
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Recipe' }}
      </button>
    </div>

    <div v-if="error" class="mx-4 mb-4 p-3 bg-red-50 border border-red-200 rounded-md flex justify-between items-center">
      <span class="text-sm text-red-700">{{ error }}</span>
      <button @click="error = null" class="text-red-400 hover:text-red-600"><i class="mdi mdi-close"></i></button>
    </div>

    <!-- Create Food Item Dialog -->
    <div v-if="showCreateFoodItemDialog" class="fixed inset-0 z-50 flex items-center justify-center">
      <div class="fixed inset-0 bg-black/50" @click="showCreateFoodItemDialog = false"></div>
      <div class="relative bg-white rounded-lg shadow-xl max-w-[600px] w-full mx-4">
        <div class="px-6 py-4 border-b border-gray-200">
          <h3 class="text-lg font-semibold text-gray-900">Create New Food Item</h3>
        </div>
        <div class="px-6 py-4">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-1">Food Item Name *</label>
            <input v-model="newFoodItem.fooditem_name" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
            <textarea v-model="newFoodItem.fooditem_description" rows="2" class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
          </div>
        </div>
        <div class="flex justify-between items-center px-6 py-4 border-t border-gray-200">
          <button type="button" class="px-4 py-2 text-sm text-gray-600 hover:text-gray-800" @click="showCreateFoodItemDialog = false">Cancel</button>
          <button type="button" class="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700 disabled:opacity-50" :disabled="creatingFoodItem" @click="createFoodItem">
            {{ creatingFoodItem ? 'Creating...' : 'Create' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Create Ingredient Dialog -->
    <div v-if="showCreateIngredientDialog" class="fixed inset-0 z-50 flex items-center justify-center">
      <div class="fixed inset-0 bg-black/50" @click="showCreateIngredientDialog = false"></div>
      <div class="relative bg-white rounded-lg shadow-xl max-w-[600px] w-full mx-4">
        <div class="px-6 py-4 border-b border-gray-200">
          <h3 class="text-lg font-semibold text-gray-900">Create New Ingredient</h3>
        </div>
        <div class="px-6 py-4">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-1">Ingredient Name *</label>
            <input v-model="newIngredient.ingredient_name" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
            <textarea v-model="newIngredient.ingredient_description" rows="2" class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
          </div>
        </div>
        <div class="flex justify-between items-center px-6 py-4 border-t border-gray-200">
          <button type="button" class="px-4 py-2 text-sm text-gray-600 hover:text-gray-800" @click="showCreateIngredientDialog = false">Cancel</button>
          <button type="button" class="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700 disabled:opacity-50" :disabled="creatingIngredient" @click="createIngredient">
            {{ creatingIngredient ? 'Creating...' : 'Create' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, computed, watch } from 'vue'

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
  name: props.initialData?.name || props.initialData?.recipe_name || '',
  description: props.initialData?.description || props.initialData?.recipe_description || '',
  fooditem_id: props.initialData?.fooditem_id || props.initialData?.recipe_fooditem_id || null,
  category_ids: props.initialData?.category_ids || []
})

// Data lists
const foodItems = ref([])
const rawIngredients = ref([])
const unitTypes = ref([])
const categories = ref([])

// Loading states
const loadingFoodItems = ref(false)
const loadingIngredients = ref(false)
const loadingUnitTypes = ref(false)
const loadingCategories = ref(false)

// Autocomplete state - Produces Food Item
const foodItemDropdownRef = ref(null)
const foodItemDropdownOpen = ref(false)
const foodItemSearch = ref('')

const filteredFoodItemsForRecipe = computed(() => {
  const q = foodItemSearch.value.toLowerCase()
  return foodItems.value.filter(f => f.fooditem_name.toLowerCase().includes(q))
})

function selectProducesFoodItem(fi) {
  formData.value.fooditem_id = fi.fooditem_id
  foodItemSearch.value = fi.fooditem_name
  foodItemDropdownOpen.value = false
}

// Autocomplete state - Ingredient sources
const ingredientDropdownRefs = ref([])
const ingredientDropdownOpenIndex = ref(null)
const ingredientSearches = ref([])

function filteredIngredientSources(index) {
  const q = (ingredientSearches.value[index] || '').toLowerCase()
  return allIngredientSources.value.filter(s => s.name.toLowerCase().includes(q))
}

function selectIngredientSource(index, src) {
  ingredients.value[index].source = src
  ingredientSearches.value[index] = src.name
  ingredientDropdownOpenIndex.value = null
}

// Autocomplete state - Recipe Categories (multi-select)
const recipeCategoryDropdownRef = ref(null)
const recipeCategoryDropdownOpen = ref(false)
const recipeCategorySearch = ref('')

const filteredRecipeCategories = computed(() => {
  const q = recipeCategorySearch.value.toLowerCase()
  return categories.value.filter(c => c.category_name.toLowerCase().includes(q))
})

function getRecipeCategoryName(catId) {
  const cat = categories.value.find(c => c.category_id === catId)
  return cat ? cat.category_name : catId
}

function toggleRecipeCategory(catId) {
  const idx = formData.value.category_ids.indexOf(catId)
  if (idx >= 0) {
    formData.value.category_ids.splice(idx, 1)
  } else {
    formData.value.category_ids.push(catId)
  }
}

function removeRecipeCategory(catId) {
  const idx = formData.value.category_ids.indexOf(catId)
  if (idx >= 0) formData.value.category_ids.splice(idx, 1)
}

// Click outside handler for all dropdowns
function handleClickOutside(e) {
  if (foodItemDropdownRef.value && !foodItemDropdownRef.value.contains(e.target)) {
    foodItemDropdownOpen.value = false
  }
  if (ingredientDropdownOpenIndex.value !== null) {
    const ref = ingredientDropdownRefs.value[ingredientDropdownOpenIndex.value]
    if (ref && !ref.contains(e.target)) {
      ingredientDropdownOpenIndex.value = null
    }
  }
  if (recipeCategoryDropdownRef.value && !recipeCategoryDropdownRef.value.contains(e.target)) {
    recipeCategoryDropdownOpen.value = false
  }
}

// Initialize search texts from data
function initSearchTexts() {
  // Food item
  if (formData.value.fooditem_id) {
    const fi = foodItems.value.find(f => f.fooditem_id === formData.value.fooditem_id)
    if (fi) foodItemSearch.value = fi.fooditem_name
  }
  // Ingredients
  ingredientSearches.value = ingredients.value.map(ing => {
    return ing.source ? ing.source.name : ''
  })
}

// Helper function to initialize ingredients from initialData
const initializeIngredients = () => {
  if (props.initialData?.ingredients && Array.isArray(props.initialData.ingredients)) {
    return props.initialData.ingredients.map(ing => {
      // Determine if it's an ingredient or food item
      if (ing.ri_ingredient_id) {
        return {
          source: {
            id: `ingredient_${ing.ri_ingredient_id}`,
            name: `${ing.ingredient_name || 'Unknown'} (ingredient)`,
            type: 'ingredient',
            originalId: ing.ri_ingredient_id
          },
          ri_quantity: ing.ri_quantity,
          ri_unit_type_id: ing.ri_unit_type_id
        }
      } else if (ing.ri_fooditem_id) {
        return {
          source: {
            id: `fooditem_${ing.ri_fooditem_id}`,
            name: `${ing.fooditem_name || 'Unknown'} (food item)`,
            type: 'fooditem',
            originalId: ing.ri_fooditem_id
          },
          ri_quantity: ing.ri_quantity,
          ri_unit_type_id: ing.ri_unit_type_id
        }
      }
      // Fallback for malformed data
      return {
        source: null,
        ri_quantity: ing.ri_quantity || null,
        ri_unit_type_id: ing.ri_unit_type_id || null
      }
    })
  }
  return [
    {
      source: null,
      ri_quantity: null,
      ri_unit_type_id: null
    }
  ]
}

// Helper function to initialize instructions from initialData
const initializeInstructions = () => {
  if (props.initialData?.instructions && Array.isArray(props.initialData.instructions)) {
    return props.initialData.instructions.map(inst => ({
      step_number: inst.step_number,
      instruction_text: inst.instruction_text || ''
    }))
  }
  return [{ step_number: 1, instruction_text: '' }]
}

// Ingredients section
const ingredients = ref(initializeIngredients())

// Instructions section
const instructions = ref(initializeInstructions())

// Inline creation dialogs
const showCreateFoodItemDialog = ref(false)
const showCreateIngredientDialog = ref(false)
const creatingFoodItem = ref(false)
const creatingIngredient = ref(false)
const currentIngredientIndex = ref(null)

const newFoodItem = ref({
  fooditem_name: '',
  fooditem_description: ''
})

const newIngredient = ref({
  ingredient_name: '',
  ingredient_description: ''
})

// Computed: Combine ingredients and food items for selection
const allIngredientSources = computed(() => {
  const sources = []

  // Add raw ingredients
  rawIngredients.value.forEach(ing => {
    sources.push({
      id: `ingredient_${ing.ingredient_id}`,
      name: `${ing.ingredient_name} (ingredient)`,
      type: 'ingredient',
      originalId: ing.ingredient_id
    })
  })

  // Add food items
  foodItems.value.forEach(item => {
    sources.push({
      id: `fooditem_${item.fooditem_id}`,
      name: `${item.fooditem_name} (food item)`,
      type: 'fooditem',
      originalId: item.fooditem_id
    })
  })

  return sources
})

// Load data
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

const loadIngredients = async () => {
  loadingIngredients.value = true
  try {
    const response = await fetch(`${API_BASE}/ingredients`)
    const data = await response.json()
    rawIngredients.value = data.ingredients || []
  } catch (err) {
    console.error('Failed to load ingredients:', err)
  } finally {
    loadingIngredients.value = false
  }
}

const loadUnitTypes = async () => {
  loadingUnitTypes.value = true
  try {
    const response = await fetch(`${API_BASE}/unit-types`)
    const data = await response.json()
    unitTypes.value = data.unit_types || []
  } catch (err) {
    console.error('Failed to load unit types:', err)
  } finally {
    loadingUnitTypes.value = false
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

// Ingredient management
const addIngredient = () => {
  ingredients.value.push({
    source: null,
    ri_quantity: null,
    ri_unit_type_id: null
  })
  ingredientSearches.value.push('')
}

const removeIngredient = (index) => {
  if (ingredients.value.length > 1) {
    ingredients.value.splice(index, 1)
    ingredientSearches.value.splice(index, 1)
  }
}

const openCreateIngredientDialog = (index) => {
  currentIngredientIndex.value = index
  ingredientDropdownOpenIndex.value = null
  showCreateIngredientDialog.value = true
}

const createIngredient = async () => {
  if (!newIngredient.value.ingredient_name) return

  creatingIngredient.value = true
  try {
    const response = await fetch(`${API_BASE}/ingredients`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newIngredient.value)
    })

    if (!response.ok) throw new Error('Failed to create ingredient')

    const created = await response.json()

    // Add to list
    rawIngredients.value.push(created)

    // Select it for current ingredient
    if (currentIngredientIndex.value !== null) {
      const source = {
        id: `ingredient_${created.ingredient_id}`,
        name: `${created.ingredient_name} (ingredient)`,
        type: 'ingredient',
        originalId: created.ingredient_id
      }
      ingredients.value[currentIngredientIndex.value].source = source
      ingredientSearches.value[currentIngredientIndex.value] = source.name
    }

    // Reset and close
    newIngredient.value = { ingredient_name: '', ingredient_description: '' }
    showCreateIngredientDialog.value = false
    currentIngredientIndex.value = null
  } catch (err) {
    console.error('Failed to create ingredient:', err)
    alert('Failed to create ingredient')
  } finally {
    creatingIngredient.value = false
  }
}

// Food item creation
const createFoodItem = async () => {
  if (!newFoodItem.value.fooditem_name) return

  creatingFoodItem.value = true
  try {
    const response = await fetch(`${API_BASE}/food-items`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newFoodItem.value)
    })

    if (!response.ok) throw new Error('Failed to create food item')

    const created = await response.json()

    // Add to list
    foodItems.value.push(created)

    // Select it
    formData.value.fooditem_id = created.fooditem_id
    foodItemSearch.value = created.fooditem_name

    // Reset and close
    newFoodItem.value = { fooditem_name: '', fooditem_description: '' }
    showCreateFoodItemDialog.value = false
  } catch (err) {
    console.error('Failed to create food item:', err)
    alert('Failed to create food item')
  } finally {
    creatingFoodItem.value = false
  }
}

// Instruction management
const addInstruction = () => {
  instructions.value.push({
    step_number: instructions.value.length + 1,
    instruction_text: ''
  })
}

const removeInstruction = (index) => {
  if (instructions.value.length > 1) {
    instructions.value.splice(index, 1)
    // Renumber steps
    instructions.value.forEach((inst, idx) => {
      inst.step_number = idx + 1
    })
  }
}

// Validation
function validate() {
  errors.value = {}
  if (!formData.value.name) {
    errors.value.name = 'Recipe name is required'
  }
  if (!formData.value.fooditem_id) {
    errors.value.fooditem_id = 'Must select which food item this recipe produces'
  }
  const hasValidIngredient = ingredients.value.some(ing => ing.source && ing.ri_quantity > 0 && ing.ri_unit_type_id)
  if (!hasValidIngredient) {
    errors.value.ingredients = 'At least one complete ingredient is required'
  }
  const hasValidInstruction = instructions.value.some(inst => inst.instruction_text.trim())
  if (!hasValidInstruction) {
    errors.value.instructions = 'At least one instruction is required'
  }
  return Object.keys(errors.value).length === 0
}

// Form submission
const handleSubmit = async () => {
  if (!validate()) return

  // Build recipe data
  const recipeData = {
		name: formData.value.name,
		description: formData.value.description,
		fooditem_id: formData.value.fooditem_id,
		category_ids: formData.value.category_ids,
    ingredients: ingredients.value.map(ing => ({
      ri_ingredient_id: ing.source?.type === 'ingredient' ? ing.source.originalId : null,
      ri_fooditem_id: ing.source?.type === 'fooditem' ? ing.source.originalId : null,
      ri_quantity: ing.ri_quantity,
      ri_unit_type_id: ing.ri_unit_type_id
    })),
    instructions: instructions.value
  }

  emit('submit', recipeData)
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  loadFoodItems()
  loadIngredients()
  loadUnitTypes()
  loadCategories()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Watch for data loading to initialize search texts
watch([foodItems, rawIngredients], () => {
  initSearchTexts()
})

// Watch for initialData changes (handles async loading)
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      name: newData.name || newData.recipe_name || '',
      description: newData.description || newData.recipe_description || '',
      fooditem_id: newData.fooditem_id || newData.recipe_fooditem_id || null,
      category_ids: newData.category_ids || []
    }

    // Update ingredients from the new data
    if (newData.ingredients && Array.isArray(newData.ingredients)) {
      ingredients.value = newData.ingredients.map(ing => {
        if (ing.ri_ingredient_id) {
          return {
            source: {
              id: `ingredient_${ing.ri_ingredient_id}`,
              name: `${ing.ingredient_name || 'Unknown'} (ingredient)`,
              type: 'ingredient',
              originalId: ing.ri_ingredient_id
            },
            ri_quantity: ing.ri_quantity,
            ri_unit_type_id: ing.ri_unit_type_id
          }
        } else if (ing.ri_fooditem_id) {
          return {
            source: {
              id: `fooditem_${ing.ri_fooditem_id}`,
              name: `${ing.fooditem_name || 'Unknown'} (food item)`,
              type: 'fooditem',
              originalId: ing.ri_fooditem_id
            },
            ri_quantity: ing.ri_quantity,
            ri_unit_type_id: ing.ri_unit_type_id
          }
        }
        return {
          source: null,
          ri_quantity: ing.ri_quantity || null,
          ri_unit_type_id: ing.ri_unit_type_id || null
        }
      })
    }

    // Update instructions from the new data
    if (newData.instructions && Array.isArray(newData.instructions)) {
      instructions.value = newData.instructions.map(inst => ({
        step_number: inst.step_number,
        instruction_text: inst.instruction_text || ''
      }))
    }

    initSearchTexts()
  }
}, { immediate: true })
</script>

<template>
  <div class="mb-4">
    <label class="block text-sm font-medium text-gray-700 mb-1">Produces Food Item *</label>

    <!-- Collapsed summary view -->
    <div
      v-if="!expanded"
      class="flex items-center gap-2 px-3 py-2 border border-gray-200 rounded-md bg-gray-50"
      :class="error ? 'border-red-300 bg-red-50' : 'border-gray-200 bg-gray-50'"
    >
      <span v-if="mode === 'new'" class="text-sm text-gray-700 flex-1 min-w-0">
        <span class="font-medium truncate">{{ displayName }}</span>
        <span class="ml-1.5 text-xs text-gray-400 italic whitespace-nowrap">(new food item will be created)</span>
      </span>
      <span v-else class="text-sm text-gray-700 flex-1 min-w-0">
        <span class="font-medium truncate">{{ selectedFoodItemName || 'No food item selected' }}</span>
        <span class="ml-1.5 text-xs text-gray-400 italic whitespace-nowrap">(existing food item)</span>
      </span>
      <button
        type="button"
        class="text-xs text-blue-600 hover:text-blue-800 hover:underline whitespace-nowrap flex-shrink-0"
        @click="expanded = true"
      >
        Edit Food Item
      </button>
    </div>

    <!-- Expanded edit panel -->
    <div v-else class="border border-blue-200 rounded-md bg-white p-4 shadow-sm">
      <!-- Mode toggle -->
      <div class="flex gap-6 mb-4">
        <label class="flex items-center gap-2 text-sm cursor-pointer select-none">
          <input
            type="radio"
            :checked="mode === 'new'"
            name="produces-food-item-mode"
            value="new"
            class="text-blue-600 focus:ring-blue-500"
            @change="onModeChange('new')"
          />
          <span>Create new food item</span>
        </label>
        <label class="flex items-center gap-2 text-sm cursor-pointer select-none">
          <input
            type="radio"
            :checked="mode === 'existing'"
            name="produces-food-item-mode"
            value="existing"
            class="text-blue-600 focus:ring-blue-500"
            @change="onModeChange('existing')"
          />
          <span>Use existing food item</span>
        </label>
      </div>

      <!-- New food item form -->
      <div v-if="mode === 'new'" class="space-y-3">
        <div>
          <label class="block text-xs font-medium text-gray-600 mb-1">Food Item Name *</label>
          <input
            v-model="newName"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="nameError ? 'border-red-500' : 'border-gray-300'"
            placeholder="e.g. Banana Bread"
            @input="onNameInput"
          />
          <p v-if="nameError" class="mt-1 text-xs text-red-600">{{ nameError }}</p>
        </div>
        <div>
          <label class="block text-xs font-medium text-gray-600 mb-1">Description</label>
          <textarea
            v-model="newDescription"
            rows="2"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Optional description"
          ></textarea>
        </div>
      </div>

      <!-- Existing food item selector -->
      <div v-else class="relative" ref="dropdownRef">
        <label class="block text-xs font-medium text-gray-600 mb-1">Search Food Items *</label>
        <input
          v-model="searchQuery"
          type="text"
          class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          :class="selectionError ? 'border-red-500' : 'border-gray-300'"
          placeholder="Search food items..."
          @focus="dropdownOpen = true"
          @input="dropdownOpen = true"
        />
        <div
          v-if="dropdownOpen"
          class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-md shadow-lg max-h-48 overflow-y-auto"
        >
          <button
            v-for="fi in filteredFoodItems"
            :key="fi.fooditem_id"
            type="button"
            class="w-full text-left px-3 py-2 text-sm hover:bg-blue-50 transition-colors"
            :class="selectedFoodItemId === fi.fooditem_id ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700'"
            @click="selectFoodItem(fi)"
          >
            {{ fi.fooditem_name }}
          </button>
          <div
            v-if="filteredFoodItems.length === 0"
            class="px-3 py-2 text-sm text-gray-500 italic"
          >
            No food items found
          </div>
        </div>
        <p v-if="selectionError" class="mt-1 text-xs text-red-600">{{ selectionError }}</p>
      </div>

      <!-- Done button -->
      <div class="flex justify-end mt-4 pt-3 border-t border-gray-100">
        <button
          type="button"
          class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-50 border border-blue-200 rounded-md hover:bg-blue-100 transition-colors"
          @click="closePanel"
        >
          Done
        </button>
      </div>
    </div>

    <p v-if="error" class="mt-1 text-xs text-red-600">{{ error }}</p>
    <p v-else-if="!expanded" class="mt-1 text-xs text-gray-500">
      {{
        mode === 'new'
          ? 'A new food item will be created automatically when the recipe is saved.'
          : 'This recipe produces the selected food item.'
      }}
    </p>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

const props = defineProps({
  /**
   * modelValue shape:
   *   { mode: 'new',      name: string, description: string }
   *   { mode: 'existing', fooditem_id: number }
   */
  modelValue: {
    type: Object,
    default: null
  },
  /** Kept in sync with the recipe name; auto-populates the new food item name. */
  recipeName: {
    type: String,
    default: ''
  },
  /** Validation error message surfaced by the parent form. */
  error: {
    type: String,
    default: null
  }
})

const emit = defineEmits(['update:modelValue'])

// ── Internal state ──────────────────────────────────────────────────────────
const mode = ref('new')               // 'new' | 'existing'
const newName = ref('')
const newDescription = ref('')
const nameIsAutoSynced = ref(true)    // true while name hasn't been manually edited
const selectedFoodItemId = ref(null)
const expanded = ref(false)

// Food-item list (loaded once on mount)
const foodItems = ref([])
const searchQuery = ref('')
const dropdownRef = ref(null)
const dropdownOpen = ref(false)

// Local validation state for the expanded panel
const nameError = ref(null)
const selectionError = ref(null)

// ── Computed ─────────────────────────────────────────────────────────────────
const filteredFoodItems = computed(() => {
  const q = searchQuery.value.toLowerCase()
  return foodItems.value.filter(f => f.fooditem_name.toLowerCase().includes(q))
})

const selectedFoodItemName = computed(() => {
  if (!selectedFoodItemId.value) return null
  const fi = foodItems.value.find(f => f.fooditem_id === selectedFoodItemId.value)
  return fi ? fi.fooditem_name : null
})

const displayName = computed(() => newName.value || props.recipeName || '(untitled)')

// ── Data loading ─────────────────────────────────────────────────────────────
const loadFoodItems = async () => {
  try {
    const response = await fetch(`${API_BASE}/food-items`)
    const data = await response.json()
    foodItems.value = data.food_items || []
  } catch (err) {
    console.error('ProducesFoodItemField: failed to load food items:', err)
  }
}

// ── Emit helpers ─────────────────────────────────────────────────────────────
function emitValue() {
  if (mode.value === 'new') {
    emit('update:modelValue', {
      mode: 'new',
      name: newName.value,
      description: newDescription.value
    })
  } else {
    emit('update:modelValue', {
      mode: 'existing',
      fooditem_id: selectedFoodItemId.value
    })
  }
}

// ── Watchers ─────────────────────────────────────────────────────────────────

// Propagate changes up to parent
watch([mode, newName, newDescription, selectedFoodItemId], emitValue)

// Auto-sync recipe name → food item name (only while not manually overridden)
watch(
  () => props.recipeName,
  (name) => {
    if (mode.value === 'new' && nameIsAutoSynced.value) {
      newName.value = name || ''
    }
  },
  { immediate: true }
)

// Respond to external modelValue changes (e.g. initialData loaded async in edit mode)
watch(
  () => props.modelValue,
  (val) => {
    if (!val) return
    if (val.mode === 'existing' && val.fooditem_id !== selectedFoodItemId.value) {
      mode.value = 'existing'
      selectedFoodItemId.value = val.fooditem_id
      nameIsAutoSynced.value = false
      const fi = foodItems.value.find(f => f.fooditem_id === val.fooditem_id)
      if (fi) searchQuery.value = fi.fooditem_name
    } else if (val.mode === 'new') {
      mode.value = 'new'
      newName.value = val.name || ''
      newDescription.value = val.description || ''
    }
  },
  { deep: true }
)

// ── Event handlers ────────────────────────────────────────────────────────────
function onNameInput() {
  nameIsAutoSynced.value = false
  nameError.value = null
}

function onModeChange(newMode) {
  mode.value = newMode
  if (newMode === 'new' && !newName.value) {
    newName.value = props.recipeName || ''
    nameIsAutoSynced.value = true
  }
  nameError.value = null
  selectionError.value = null
}

function selectFoodItem(fi) {
  selectedFoodItemId.value = fi.fooditem_id
  searchQuery.value = fi.fooditem_name
  dropdownOpen.value = false
  selectionError.value = null
}

function closePanel() {
  // Validate before allowing collapse
  if (mode.value === 'new' && !newName.value.trim()) {
    nameError.value = 'Food item name is required'
    return
  }
  if (mode.value === 'existing' && !selectedFoodItemId.value) {
    selectionError.value = 'Please select a food item'
    return
  }
  nameError.value = null
  selectionError.value = null
  expanded.value = false
}

function handleClickOutside(e) {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target)) {
    dropdownOpen.value = false
  }
}

// ── Initialisation ────────────────────────────────────────────────────────────
function initFromModelValue() {
  if (!props.modelValue) return
  if (props.modelValue.mode === 'existing') {
    mode.value = 'existing'
    selectedFoodItemId.value = props.modelValue.fooditem_id || null
    nameIsAutoSynced.value = false
    const fi = foodItems.value.find(f => f.fooditem_id === selectedFoodItemId.value)
    if (fi) searchQuery.value = fi.fooditem_name
  } else if (props.modelValue.mode === 'new') {
    mode.value = 'new'
    newName.value = props.modelValue.name || ''
    newDescription.value = props.modelValue.description || ''
    nameIsAutoSynced.value = false
  }
}

onMounted(async () => {
  document.addEventListener('click', handleClickOutside)
  await loadFoodItems()
  initFromModelValue()
  // Emit initial value so the parent always starts with a valid model
  emitValue()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

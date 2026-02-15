<template>
  <div class="mx-auto max-w-[800px] bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Ingredient</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Ingredient Name *</label>
          <input
            v-model="formData.ingredient_name"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.ingredient_name ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.ingredient_name" class="mt-1 text-xs text-red-600">{{ errors.ingredient_name }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">e.g., Salt, Sugar, Flour</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea
            v-model="formData.ingredient_description"
            rows="3"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
          <p class="mt-1 text-xs text-gray-500">Optional description of the ingredient</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Notes</label>
          <textarea
            v-model="formData.ingredient_notes"
            rows="2"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
          <p class="mt-1 text-xs text-gray-500">Any additional notes</p>
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
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Ingredient' }}
      </button>
    </div>

    <div v-if="error" class="mx-4 mb-4 p-3 bg-red-50 border border-red-200 rounded-md flex justify-between items-center">
      <span class="text-sm text-red-700">{{ error }}</span>
      <button @click="error = null" class="text-red-400 hover:text-red-600"><i class="mdi mdi-close"></i></button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'

const props = defineProps({
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  },
  initialData: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isEditMode = computed(() => !!props.initialData)

const errors = ref({})
const formData = ref({
  ingredient_name: props.initialData?.ingredient_name || '',
  ingredient_description: props.initialData?.ingredient_description || '',
  ingredient_notes: props.initialData?.ingredient_notes || ''
})

// Watch for initialData changes (when it loads async)
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      ingredient_name: newData.ingredient_name || '',
      ingredient_description: newData.ingredient_description || '',
      ingredient_notes: newData.ingredient_notes || ''
    }
  }
}, { immediate: true })

function validate() {
  errors.value = {}
  if (!formData.value.ingredient_name) {
    errors.value.ingredient_name = 'Name is required'
  }
  return Object.keys(errors.value).length === 0
}

const handleSubmit = async () => {
  if (validate()) {
    emit('submit', formData.value)
  }
}
</script>

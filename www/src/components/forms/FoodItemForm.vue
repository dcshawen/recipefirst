<template>
  <div class="mx-auto max-w-[800px] bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Food Item</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <div class="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-md">
        <span class="text-sm text-blue-800">Recipes that produce this food item can be linked when creating or editing recipes.</span>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Food Item Name *</label>
          <input
            v-model="formData.fooditem_name"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.fooditem_name ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.fooditem_name" class="mt-1 text-xs text-red-600">{{ errors.fooditem_name }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">e.g., Bread, Pasta, Chicken Breast</p>
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea
            v-model="formData.fooditem_description"
            rows="3"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
          <p class="mt-1 text-xs text-gray-500">Optional description</p>
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
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Food Item' }}
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
  loading: Boolean,
  error: String,
  initialData: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isEditMode = computed(() => !!props.initialData)

const errors = ref({})
const formData = ref({
  fooditem_name: props.initialData?.fooditem_name || '',
  fooditem_description: props.initialData?.fooditem_description || ''
})

// Watch for initialData changes
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      fooditem_name: newData.fooditem_name || '',
      fooditem_description: newData.fooditem_description || ''
    }
  }
}, { immediate: true })

function validate() {
  errors.value = {}
  if (!formData.value.fooditem_name) {
    errors.value.fooditem_name = 'Name is required'
  }
  return Object.keys(errors.value).length === 0
}

const handleSubmit = async () => {
  if (validate()) {
    emit('submit', formData.value)
  }
}
</script>

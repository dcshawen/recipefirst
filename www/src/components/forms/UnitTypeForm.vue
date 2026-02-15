<template>
  <div class="mx-auto max-w-[800px] bg-white rounded-lg shadow border border-gray-200">
    <div class="px-6 py-4">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Unit Type</h2>
    </div>

    <hr class="border-gray-200" />

    <div class="px-6 py-4">
      <div class="mb-4 p-3 bg-amber-50 border border-amber-200 rounded-md">
        <span class="text-sm text-amber-800">Unit type must be unique. Check existing units before creating.</span>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Unit Type *</label>
          <input
            v-model="formData.unit_type"
            type="text"
            class="w-full px-3 py-2 border rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            :class="errors.unit_type ? 'border-red-500' : 'border-gray-300'"
          />
          <p v-if="errors.unit_type" class="mt-1 text-xs text-red-600">{{ errors.unit_type }}</p>
          <p v-else class="mt-1 text-xs text-gray-500">e.g., cup, tablespoon, gram, ounce</p>
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
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Unit Type' }}
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
  unit_type: props.initialData?.unit_type || ''
})

// Watch for initialData changes
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      unit_type: newData.unit_type || ''
    }
  }
}, { immediate: true })

function validate() {
  errors.value = {}
  if (!formData.value.unit_type) {
    errors.value.unit_type = 'Unit type is required'
  } else if (!/^[a-zA-Z\s]+$/.test(formData.value.unit_type)) {
    errors.value.unit_type = 'Only letters and spaces allowed'
  }
  return Object.keys(errors.value).length === 0
}

const handleSubmit = async () => {
  if (validate()) {
    emit('submit', formData.value)
  }
}
</script>

<template>
  <div class="mx-auto max-w-3xl card">
    <div class="card-header">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Ingredient</h2>
    </div>

    <div class="card-body">
      <form @submit.prevent="handleSubmit">
        <div class="mb-5">
          <label class="form-label">Ingredient Name *</label>
          <input
            v-model="formData.ingredient_name"
            type="text"
            class="form-input"
            :class="{ 'is-error': errors.ingredient_name }"
          />
          <p v-if="errors.ingredient_name" class="form-error">{{ errors.ingredient_name }}</p>
          <p v-else class="form-hint">e.g., Salt, Sugar, Flour</p>
        </div>

        <div class="mb-5">
          <label class="form-label">Description</label>
          <textarea
            v-model="formData.ingredient_description"
            rows="3"
            class="form-input"
          ></textarea>
          <p class="form-hint">Optional description of the ingredient</p>
        </div>

        <div class="mb-5">
          <label class="form-label">Notes</label>
          <textarea
            v-model="formData.ingredient_notes"
            rows="2"
            class="form-input"
          ></textarea>
          <p class="form-hint">Any additional notes</p>
        </div>
      </form>
    </div>

    <div class="card-footer flex justify-between items-center">
      <button type="button" class="btn btn-ghost" :disabled="loading" @click="$emit('cancel')">
        Cancel
      </button>
      <button type="button" class="btn btn-primary" :disabled="loading" @click="handleSubmit">
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Ingredient' }}
      </button>
    </div>

    <div v-if="error" class="mx-4 mb-4 alert alert-error">
      <span>{{ error }}</span>
      <button @click="error = null" class="text-danger-500 hover:text-danger-700"><i class="mdi mdi-close"></i></button>
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

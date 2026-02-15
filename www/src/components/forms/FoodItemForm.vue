<template>
  <div class="mx-auto max-w-3xl card">
    <div class="card-header">
      <h2 class="text-xl font-semibold text-gray-900">{{ isEditMode ? 'Edit' : 'Create New' }} Food Item</h2>
    </div>

    <div class="card-body">
      <div class="alert alert-info mb-5">
        <span>Recipes that produce this food item can be linked when creating or editing recipes.</span>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="mb-5">
          <label class="form-label">Food Item Name *</label>
          <input
            v-model="formData.fooditem_name"
            type="text"
            class="form-input"
            :class="{ 'is-error': errors.fooditem_name }"
          />
          <p v-if="errors.fooditem_name" class="form-error">{{ errors.fooditem_name }}</p>
          <p v-else class="form-hint">e.g., Bread, Pasta, Chicken Breast</p>
        </div>

        <div class="mb-5">
          <label class="form-label">Description</label>
          <textarea
            v-model="formData.fooditem_description"
            rows="3"
            class="form-input"
          ></textarea>
          <p class="form-hint">Optional description</p>
        </div>
      </form>
    </div>

    <div class="card-footer flex justify-between items-center">
      <button type="button" class="btn btn-ghost" :disabled="loading" @click="$emit('cancel')">
        Cancel
      </button>
      <button type="button" class="btn btn-primary" :disabled="loading" @click="handleSubmit">
        {{ loading ? 'Saving...' : (isEditMode ? 'Update' : 'Create') + ' Food Item' }}
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

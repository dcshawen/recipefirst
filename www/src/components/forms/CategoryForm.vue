<template>
  <v-card class="mx-auto" max-width="800">
    <v-card-title class="text-h5 py-4">
      {{ isEditMode ? 'Edit' : 'Create New' }} Category
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <v-text-field
          v-model="formData.category_name"
          label="Category Name *"
          :rules="[(v) => !!v || 'Name is required']"
          hint="e.g., Breakfast, Vegetarian, Italian"
          persistent-hint
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="formData.category_description"
          label="Description"
          rows="2"
          class="mb-4"
        ></v-textarea>

        <v-autocomplete
          v-model="formData.parent_category_id"
          :items="categories"
          item-title="category_name"
          item-value="category_id"
          label="Parent Category"
          hint="Optional: Select a parent category for hierarchy"
          persistent-hint
          clearable
          :loading="loadingCategories"
        ></v-autocomplete>
      </v-form>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="pa-4">
      <v-btn color="grey" variant="text" @click="$emit('cancel')" :disabled="loading">
        Cancel
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn color="primary" variant="elevated" @click="handleSubmit" :loading="loading">
        {{ isEditMode ? 'Update' : 'Create' }} Category
      </v-btn>
    </v-card-actions>

    <v-alert v-if="error" type="error" class="ma-4" closable @click:close="error = null">
      {{ error }}
    </v-alert>
  </v-card>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue'

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

const formRef = ref(null)
const formData = ref({
  category_name: props.initialData?.category_name || '',
  category_description: props.initialData?.category_description || '',
  parent_category_id: props.initialData?.parent_category_id || null
})

const categories = ref([])
const loadingCategories = ref(false)

// Watch for initialData changes
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      category_name: newData.category_name || '',
      category_description: newData.category_description || '',
      parent_category_id: newData.parent_category_id || null
    }
  }
}, { immediate: true })

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

const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (valid) {
    emit('submit', formData.value)
  }
}

onMounted(() => {
  loadCategories()
})
</script>

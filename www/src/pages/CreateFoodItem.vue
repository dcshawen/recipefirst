<template>
  <div class="p-6">
    <v-breadcrumbs :items="breadcrumbs" divider="›" class="px-0"></v-breadcrumbs>

    <FoodItemForm
      :loading="loading"
      :error="error"
      @submit="handleCreate"
      @cancel="cancel"
    />

    <v-snackbar v-model="showSuccess" color="success" timeout="3000" location="top">
      Food Item created successfully!
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import FoodItemForm from '../components/forms/FoodItemForm.vue'
import { useEntityCreate } from '../composables/useEntityCreate'

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Food Items', to: '/fooditems' },
  { title: 'Create New', disabled: true }
]

const { loading, error, createEntity, cancel } = useEntityCreate('food-items', {
  redirectPath: '/fooditems',
  idField: 'fooditem_id'
})

const showSuccess = ref(false)

const handleCreate = async (data) => {
  try {
    await createEntity(data)
    showSuccess.value = true
  } catch (err) {
    // Error handling is done in composable
  }
}
</script>

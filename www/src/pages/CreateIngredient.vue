<template>
  <div class="p-6">
    <v-breadcrumbs :items="breadcrumbs" divider="›" class="px-0"></v-breadcrumbs>

    <IngredientForm
      :loading="loading"
      :error="error"
      @submit="handleCreate"
      @cancel="cancel"
    />

    <v-snackbar
      v-model="showSuccess"
      color="success"
      timeout="3000"
      location="top"
    >
      Ingredient created successfully!
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import IngredientForm from '../components/forms/IngredientForm.vue'
import { useEntityCreate } from '../composables/useEntityCreate'

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Ingredients', to: '/ingredients' },
  { title: 'Create New', disabled: true }
]

const { loading, error, createEntity, cancel } = useEntityCreate('ingredients', {
  idField: 'ingredient_id'
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

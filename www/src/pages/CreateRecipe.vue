<template>
  <div class="p-6">
    <RecipeForm
      :loading="loading"
      :error="error"
      @submit="handleCreate"
      @cancel="cancel"
    />

    <div v-if="showSuccess" class="fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-green-600 text-white px-6 py-3 rounded-md shadow-lg text-sm">
      Recipe created successfully!
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import RecipeForm from '../components/forms/RecipeForm.vue'
import { useEntityCreate } from '../composables/useEntityCreate'

const { loading, error, createEntity, cancel } = useEntityCreate('recipes', {
  idField: 'recipe_id'
})

const showSuccess = ref(false)
watch(showSuccess, (val) => { if (val) setTimeout(() => { showSuccess.value = false }, 3000) })

const handleCreate = async (data) => {
  try {
    await createEntity(data)
    showSuccess.value = true
  } catch (err) {
    // Error handling is done in composable
  }
}
</script>

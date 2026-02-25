<template>
  <div class="p-6">
    <IngredientForm
      :loading="loading"
      :error="error"
      :initial-data="data"
      @submit="handleUpdate"
      @cancel="cancel"
    />

    <div v-if="showSuccess" class="fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-green-600 text-white px-6 py-3 rounded-md shadow-lg text-sm">
      Ingredient updated successfully!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import IngredientForm from '../components/forms/IngredientForm.vue'
import { useEntityUpdate } from '../composables/useEntityUpdate'

const route = useRoute()
const id = route.params.id

const { loading, error, data, fetchEntity, updateEntity, cancel } = useEntityUpdate('ingredients', id, {
  idField: 'ingredient_id'
})

const showSuccess = ref(false)
watch(showSuccess, (val) => { if (val) setTimeout(() => { showSuccess.value = false }, 3000) })

const handleUpdate = async (formData) => {
  try {
    await updateEntity(formData)
    showSuccess.value = true
  } catch (err) {
    // Error handling is done in composable
  }
}

onMounted(() => {
  fetchEntity()
})
</script>

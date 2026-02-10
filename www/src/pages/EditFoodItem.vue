<template>
  <div class="p-6">
    <v-breadcrumbs :items="breadcrumbs" divider="›" class="px-0"></v-breadcrumbs>

    <FoodItemForm
      :loading="loading"
      :error="error"
      :initial-data="data"
      @submit="handleUpdate"
      @cancel="cancel"
    />

    <v-snackbar v-model="showSuccess" color="success" timeout="3000" location="top">
      Food Item updated successfully!
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import FoodItemForm from '../components/forms/FoodItemForm.vue'
import { useEntityUpdate } from '../composables/useEntityUpdate'

const route = useRoute()
const id = route.params.id

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Food Items', to: '/fooditems' },
  { title: `Edit Food Item #${id}`, disabled: true }
]

const { loading, error, data, fetchEntity, updateEntity, cancel } = useEntityUpdate('food-items', id, {
  redirectPath: '/fooditems',
  idField: 'fooditem_id'
})

const showSuccess = ref(false)

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

<template>
  <div class="p-6">
    <v-breadcrumbs :items="breadcrumbs" divider="›" class="px-0"></v-breadcrumbs>

    <CategoryForm
      :loading="loading"
      :error="error"
      :initial-data="data"
      @submit="handleUpdate"
      @cancel="cancel"
    />

    <v-snackbar v-model="showSuccess" color="success" timeout="3000" location="top">
      Category updated successfully!
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import CategoryForm from '../components/forms/CategoryForm.vue'
import { useEntityUpdate } from '../composables/useEntityUpdate'

const route = useRoute()
const id = route.params.id

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Categories', to: '/categories' },
  { title: `Edit Category #${id}`, disabled: true }
]

const { loading, error, data, fetchEntity, updateEntity, cancel } = useEntityUpdate('categories', id, {
  idField: 'category_id'
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

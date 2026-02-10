<template>
  <div class="p-6">
    <v-breadcrumbs :items="breadcrumbs" divider="›" class="px-0"></v-breadcrumbs>

    <UnitTypeForm
      :loading="loading"
      :error="error"
      :initial-data="data"
      @submit="handleUpdate"
      @cancel="cancel"
    />

    <v-snackbar v-model="showSuccess" color="success" timeout="3000" location="top">
      Unit Type updated successfully!
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import UnitTypeForm from '../components/forms/UnitTypeForm.vue'
import { useEntityUpdate } from '../composables/useEntityUpdate'

const route = useRoute()
const id = route.params.id

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Unit Types', to: '/unittypes' },
  { title: `Edit Unit Type #${id}`, disabled: true }
]

const { loading, error, data, fetchEntity, updateEntity, cancel } = useEntityUpdate('unit-types', id, {
  redirectPath: '/unittypes',
  idField: 'id'
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

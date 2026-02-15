<template>
  <div class="p-6">
    <nav class="flex items-center gap-1 text-sm text-gray-500 mb-4">
      <template v-for="(item, index) in breadcrumbs" :key="index">
        <span v-if="index > 0" class="mx-1">›</span>
        <router-link v-if="item.to && !item.disabled" :to="item.to" class="text-blue-600 hover:text-blue-800 hover:underline">{{ item.title }}</router-link>
        <span v-else class="text-gray-800">{{ item.title }}</span>
      </template>
    </nav>

    <MealForm
      :loading="loading"
      :error="error"
      :initial-data="data"
      @submit="handleUpdate"
      @cancel="cancel"
    />

    <div v-if="showSuccess" class="fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-green-600 text-white px-6 py-3 rounded-md shadow-lg text-sm">
      Meal updated successfully!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import MealForm from '../components/forms/MealForm.vue'
import { useEntityUpdate } from '../composables/useEntityUpdate'

const route = useRoute()
const id = route.params.id

const breadcrumbs = [
  { title: 'Home', to: '/' },
  { title: 'Meals', to: '/meals' },
  { title: `Edit Meal #${id}`, disabled: true }
]

const { loading, error, data, fetchEntity, updateEntity, cancel } = useEntityUpdate('meals', id, {
  idField: 'meal_id'
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

<template>
  <div class="p-6">
    <nav class="flex items-center gap-1 text-sm text-gray-500 mb-4">
      <template v-for="(item, index) in breadcrumbs" :key="index">
        <span v-if="index > 0" class="mx-1">›</span>
        <router-link v-if="item.to && !item.disabled" :to="item.to" class="text-blue-600 hover:text-blue-800 hover:underline">{{ item.title }}</router-link>
        <span v-else class="text-gray-800">{{ item.title }}</span>
      </template>
    </nav>

    <FoodItemForm
      :loading="loading"
      :error="error"
      @submit="handleCreate"
      @cancel="cancel"
    />

    <div v-if="showSuccess" class="fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-green-600 text-white px-6 py-3 rounded-md shadow-lg text-sm">
      Food Item created successfully!
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
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

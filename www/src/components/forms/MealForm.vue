<template>
  <v-card class="mx-auto" width="100%">
    <v-card-title class="text-h5 py-4">
      Create New Meal
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <!-- Basic Information -->
        <v-text-field
          v-model="formData.meal_name"
          label="Meal Name *"
          :rules="[(v) => !!v || 'Meal name is required']"
          hint="e.g., Sunday Dinner, Weekday Lunch"
          persistent-hint
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="formData.meal_description"
          label="Description"
          rows="3"
          class="mb-4"
        ></v-textarea>

        <v-divider class="my-6"></v-divider>

        <!-- Food Items Selection -->
        <h3 class="text-h6 mb-3">Food Items *</h3>

        <div v-for="(item, index) in selectedFoodItems" :key="index" class="mb-4 pa-4 bg-grey-lighten-4 rounded">
          <v-row>
            <v-col cols="12" md="11">
              <v-autocomplete
                v-model="item.fooditem_id"
                :items="foodItems"
                item-title="fooditem_name"
                item-value="fooditem_id"
                label="Food Item *"
                :rules="[(v) => !!v || 'Required']"
                :loading="loadingFoodItems"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" md="1" class="d-flex align-center">
              <v-btn
                icon="mdi-delete"
                color="error"
                variant="text"
                size="small"
                @click="removeFoodItem(index)"
                :disabled="selectedFoodItems.length === 1"
              ></v-btn>
            </v-col>
          </v-row>
        </div>

        <v-btn
          prepend-icon="mdi-plus"
          variant="outlined"
          color="primary"
          @click="addFoodItem"
          class="mb-6"
        >
          Add Food Item
        </v-btn>

        <v-divider class="my-6"></v-divider>

        <!-- Categories Selection -->
        <h3 class="text-h6 mb-3">Categories (Optional)</h3>
        <v-autocomplete
          v-model="formData.category_ids"
          :items="categories"
          item-title="category_name"
          item-value="category_id"
          label="Select Categories"
          multiple
          chips
          closable-chips
          :loading="loadingCategories"
          hint="Optional: Select one or more categories"
          persistent-hint
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
        Create Meal
      </v-btn>
    </v-card-actions>

    <v-alert v-if="error" type="error" class="ma-4" closable @click:close="error = null">
      {{ error }}
    </v-alert>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  loading: Boolean,
  error: String
})

const emit = defineEmits(['submit', 'cancel'])

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

const formRef = ref(null)
const formData = ref({
  meal_name: '',
  meal_description: '',
  category_ids: []
})

const selectedFoodItems = ref([
  { fooditem_id: null }
])

const foodItems = ref([])
const categories = ref([])
const loadingFoodItems = ref(false)
const loadingCategories = ref(false)

const loadFoodItems = async () => {
  loadingFoodItems.value = true
  try {
    const response = await fetch(`${API_BASE}/food-items`)
    const data = await response.json()
    foodItems.value = data.food_items || []
  } catch (err) {
    console.error('Failed to load food items:', err)
  } finally {
    loadingFoodItems.value = false
  }
}

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

const addFoodItem = () => {
  selectedFoodItems.value.push({ fooditem_id: null })
}

const removeFoodItem = (index) => {
  if (selectedFoodItems.value.length > 1) {
    selectedFoodItems.value.splice(index, 1)
  }
}

const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (valid) {
    // Extract food item IDs
    const fooditem_ids = selectedFoodItems.value.map(item => item.fooditem_id).filter(id => id !== null)

    if (fooditem_ids.length === 0) {
      alert('Please select at least one food item')
      return
    }

    const submitData = {
      ...formData.value,
      fooditem_ids
    }

    emit('submit', submitData)
  }
}

onMounted(() => {
  loadFoodItems()
  loadCategories()
})
</script>

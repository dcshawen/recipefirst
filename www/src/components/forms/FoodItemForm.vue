<template>
  <v-card class="mx-auto" max-width="800">
    <v-card-title class="text-h5 py-4">
      Create New Food Item
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-alert type="info" variant="tonal" class="mb-4">
        Recipes that produce this food item can be linked when creating or editing recipes.
      </v-alert>

      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <v-text-field
          v-model="formData.fooditem_name"
          label="Food Item Name *"
          :rules="[(v) => !!v || 'Name is required']"
          hint="e.g., Bread, Pasta, Chicken Breast"
          persistent-hint
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="formData.fooditem_description"
          label="Description"
          rows="3"
          hint="Optional description"
          persistent-hint
        ></v-textarea>
      </v-form>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="pa-4">
      <v-btn color="grey" variant="text" @click="$emit('cancel')" :disabled="loading">
        Cancel
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn color="primary" variant="elevated" @click="handleSubmit" :loading="loading">
        Create Food Item
      </v-btn>
    </v-card-actions>

    <v-alert v-if="error" type="error" class="ma-4" closable @click:close="error = null">
      {{ error }}
    </v-alert>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  loading: Boolean,
  error: String
})

const emit = defineEmits(['submit', 'cancel'])

const formRef = ref(null)
const formData = ref({
  fooditem_name: '',
  fooditem_description: ''
})

const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (valid) {
    emit('submit', formData.value)
  }
}
</script>

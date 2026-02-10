<template>
  <v-card class="mx-auto" max-width="800">
    <v-card-title class="text-h5 py-4">
      Create New Ingredient
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <v-text-field
          v-model="formData.ingredient_name"
          label="Ingredient Name *"
          :rules="[(v) => !!v || 'Name is required']"
          hint="e.g., Salt, Sugar, Flour"
          persistent-hint
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="formData.ingredient_description"
          label="Description"
          rows="3"
          hint="Optional description of the ingredient"
          persistent-hint
          class="mb-4"
        ></v-textarea>

        <v-textarea
          v-model="formData.ingredient_notes"
          label="Notes"
          rows="2"
          hint="Any additional notes"
          persistent-hint
        ></v-textarea>
      </v-form>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="pa-4">
      <v-btn
        color="grey"
        variant="text"
        @click="$emit('cancel')"
        :disabled="loading"
      >
        Cancel
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        color="primary"
        variant="elevated"
        @click="handleSubmit"
        :loading="loading"
      >
        Create Ingredient
      </v-btn>
    </v-card-actions>

    <v-alert
      v-if="error"
      type="error"
      class="ma-4"
      closable
      @click:close="error = null"
    >
      {{ error }}
    </v-alert>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const formRef = ref(null)
const formData = ref({
  ingredient_name: '',
  ingredient_description: '',
  ingredient_notes: ''
})

const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (valid) {
    emit('submit', formData.value)
  }
}
</script>

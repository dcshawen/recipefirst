<template>
  <v-card class="mx-auto" max-width="800">
    <v-card-title class="text-h5 py-4">
      {{ isEditMode ? 'Edit' : 'Create New' }} Unit Type
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-alert type="warning" variant="tonal" class="mb-4">
        Unit type must be unique. Check existing units before creating.
      </v-alert>

      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <v-text-field
          v-model="formData.unit_type"
          label="Unit Type *"
          :rules="[
            (v) => !!v || 'Unit type is required',
            (v) => /^[a-zA-Z\s]+$/.test(v) || 'Only letters and spaces allowed'
          ]"
          hint="e.g., cup, tablespoon, gram, ounce"
          persistent-hint
        ></v-text-field>
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
        {{ isEditMode ? 'Update' : 'Create' }} Unit Type
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
import { ref, watch, computed } from 'vue'

const props = defineProps({
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  },
  initialData: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isEditMode = computed(() => !!props.initialData)

const formRef = ref(null)
const formData = ref({
  unit_type: props.initialData?.unit_type || ''
})

// Watch for initialData changes
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      unit_type: newData.unit_type || ''
    }
  }
}, { immediate: true })

const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (valid) {
    emit('submit', formData.value)
  }
}
</script>

<template>
  <v-card class="mx-auto" max-width="1000">
    <v-card-title class="text-h5 py-4">
      {{ isEditMode ? 'Edit' : 'Create New' }} Recipe
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-form ref="formRef" @submit.prevent="handleSubmit">
        <!-- Basic Information -->
        <h3 class="text-h6 mb-3">Basic Information</h3>

        <v-text-field
          v-model="formData.name"
          label="Recipe Name *"
          :rules="[(v) => !!v || 'Recipe name is required']"
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="formData.description"
          label="Description"
          rows="3"
          class="mb-4"
        ></v-textarea>

        <v-autocomplete
          v-model="formData.fooditem_id"
          :items="foodItems"
          item-title="fooditem_name"
          item-value="fooditem_id"
          label="Produces Food Item *"
          :rules="[(v) => !!v || 'Must select a food item']"
          :loading="loadingFoodItems"
          hint="Select the food item this recipe produces"
          persistent-hint
          class="mb-4"
        >
          <template v-slot:append-item>
            <v-divider></v-divider>
            <v-list-item @click="showCreateFoodItemDialog = true">
              <v-list-item-title class="text-primary">
                <v-icon>mdi-plus</v-icon>
                Create New Food Item
              </v-list-item-title>
            </v-list-item>
          </template>
        </v-autocomplete>

        <v-divider class="my-6"></v-divider>

        <!-- Ingredients Section -->
        <h3 class="text-h6 mb-3">Ingredients *</h3>

        <div v-for="(ingredient, index) in ingredients" :key="index" class="mb-4 pa-4 bg-grey-lighten-4 rounded">
          <v-row>
            <v-col cols="12" md="5">
              <v-autocomplete
                v-model="ingredient.source"
                :items="allIngredientSources"
                item-title="name"
                item-value="id"
                label="Ingredient or Food Item *"
                :rules="[(v) => !!v || 'Required']"
                return-object
              >
                <template v-slot:append-item>
                  <v-divider></v-divider>
                  <v-list-item @click="openCreateIngredientDialog(index)">
                    <v-list-item-title class="text-primary">
                      <v-icon>mdi-plus</v-icon>
                      Create New Ingredient
                    </v-list-item-title>
                  </v-list-item>
                </template>
              </v-autocomplete>
            </v-col>
            <v-col cols="12" md="3">
              <v-text-field
                v-model.number="ingredient.ri_quantity"
                label="Quantity *"
                type="number"
                step="0.25"
                min="0"
                :rules="[(v) => v > 0 || 'Must be greater than 0']"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <v-select
                v-model="ingredient.ri_unit_type_id"
                :items="unitTypes"
                item-title="unit_type"
                item-value="id"
                label="Unit *"
                :rules="[(v) => !!v || 'Required']"
                :loading="loadingUnitTypes"
              ></v-select>
            </v-col>
            <v-col cols="12" md="1" class="d-flex align-center">
              <v-btn
                icon="mdi-delete"
                color="error"
                variant="text"
                size="small"
                @click="removeIngredient(index)"
                :disabled="ingredients.length === 1"
              ></v-btn>
            </v-col>
          </v-row>
        </div>

        <v-btn
          prepend-icon="mdi-plus"
          variant="outlined"
          color="primary"
          @click="addIngredient"
          class="mb-6"
        >
          Add Ingredient
        </v-btn>

        <v-divider class="my-6"></v-divider>

        <!-- Instructions Section -->
        <h3 class="text-h6 mb-3">Instructions *</h3>

        <div v-for="(instruction, index) in instructions" :key="index" class="mb-4">
          <v-textarea
            v-model="instruction.instruction_text"
            :label="`Step ${index + 1} *`"
            :rules="[(v) => !!v || 'Instruction text is required']"
            rows="2"
            class="mb-2"
          >
            <template v-slot:append>
              <v-btn
                icon="mdi-delete"
                color="error"
                variant="text"
                size="small"
                @click="removeInstruction(index)"
                :disabled="instructions.length === 1"
              ></v-btn>
            </template>
          </v-textarea>
        </div>

        <v-btn
          prepend-icon="mdi-plus"
          variant="outlined"
          color="primary"
          @click="addInstruction"
          class="mb-6"
        >
          Add Step
        </v-btn>

        <v-divider class="my-6"></v-divider>

        <!-- Categories Selection -->
        <h3 class="text-h6 mb-3">Categories (Optional)</h3>
        <v-autocomplete
          v-model="formData.category_id"
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
        {{ isEditMode ? 'Update' : 'Create' }} Recipe
      </v-btn>
    </v-card-actions>

    <v-alert v-if="error" type="error" class="ma-4" closable @click:close="error = null">
      {{ error }}
    </v-alert>

    <!-- Create Food Item Dialog -->
    <v-dialog v-model="showCreateFoodItemDialog" max-width="600">
      <v-card>
        <v-card-title>Create New Food Item</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newFoodItem.fooditem_name"
            label="Food Item Name *"
            class="mb-2"
          ></v-text-field>
          <v-textarea
            v-model="newFoodItem.fooditem_description"
            label="Description"
            rows="2"
          ></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-btn color="grey" variant="text" @click="showCreateFoodItemDialog = false">
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="createFoodItem" :loading="creatingFoodItem">
            Create
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Create Ingredient Dialog -->
    <v-dialog v-model="showCreateIngredientDialog" max-width="600">
      <v-card>
        <v-card-title>Create New Ingredient</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newIngredient.ingredient_name"
            label="Ingredient Name *"
            class="mb-2"
          ></v-text-field>
          <v-textarea
            v-model="newIngredient.ingredient_description"
            label="Description"
            rows="2"
          ></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-btn color="grey" variant="text" @click="showCreateIngredientDialog = false">
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="createIngredient" :loading="creatingIngredient">
            Create
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'

const props = defineProps({
  loading: Boolean,
  error: String,
  initialData: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isEditMode = computed(() => !!props.initialData)

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

const formRef = ref(null)
const formData = ref({
  name: props.initialData?.name || '',
  description: props.initialData?.description || '',
  fooditem_id: props.initialData?.fooditem_id || null,
  category_id: props.initialData?.category_id || []
})

// Data lists
const foodItems = ref([])
const rawIngredients = ref([])
const unitTypes = ref([])
const categories = ref([])

// Loading states
const loadingFoodItems = ref(false)
const loadingIngredients = ref(false)
const loadingUnitTypes = ref(false)
const loadingCategories = ref(false)

// Helper function to initialize ingredients from initialData
const initializeIngredients = () => {
  if (props.initialData?.ingredients && Array.isArray(props.initialData.ingredients)) {
    return props.initialData.ingredients.map(ing => {
      // Determine if it's an ingredient or food item
      if (ing.ri_ingredient_id) {
        return {
          source: {
            id: `ingredient_${ing.ri_ingredient_id}`,
            name: `${ing.ingredient_name || 'Unknown'} (ingredient)`,
            type: 'ingredient',
            originalId: ing.ri_ingredient_id
          },
          ri_quantity: ing.ri_quantity,
          ri_unit_type_id: ing.ri_unit_type_id
        }
      } else if (ing.ri_fooditem_id) {
        return {
          source: {
            id: `fooditem_${ing.ri_fooditem_id}`,
            name: `${ing.fooditem_name || 'Unknown'} (food item)`,
            type: 'fooditem',
            originalId: ing.ri_fooditem_id
          },
          ri_quantity: ing.ri_quantity,
          ri_unit_type_id: ing.ri_unit_type_id
        }
      }
      // Fallback for malformed data
      return {
        source: null,
        ri_quantity: ing.ri_quantity || null,
        ri_unit_type_id: ing.ri_unit_type_id || null
      }
    })
  }
  return [
    {
      source: null,
      ri_quantity: null,
      ri_unit_type_id: null
    }
  ]
}

// Helper function to initialize instructions from initialData
const initializeInstructions = () => {
  if (props.initialData?.instructions && Array.isArray(props.initialData.instructions)) {
    return props.initialData.instructions.map(inst => ({
      step_number: inst.step_number,
      instruction_text: inst.instruction_text || ''
    }))
  }
  return [{ step_number: 1, instruction_text: '' }]
}

// Ingredients section
const ingredients = ref(initializeIngredients())

// Instructions section
const instructions = ref(initializeInstructions())

// Inline creation dialogs
const showCreateFoodItemDialog = ref(false)
const showCreateIngredientDialog = ref(false)
const creatingFoodItem = ref(false)
const creatingIngredient = ref(false)
const currentIngredientIndex = ref(null)

const newFoodItem = ref({
  fooditem_name: '',
  fooditem_description: ''
})

const newIngredient = ref({
  ingredient_name: '',
  ingredient_description: ''
})

// Computed: Combine ingredients and food items for selection
const allIngredientSources = computed(() => {
  const sources = []

  // Add raw ingredients
  rawIngredients.value.forEach(ing => {
    sources.push({
      id: `ingredient_${ing.ingredient_id}`,
      name: `${ing.ingredient_name} (ingredient)`,
      type: 'ingredient',
      originalId: ing.ingredient_id
    })
  })

  // Add food items
  foodItems.value.forEach(item => {
    sources.push({
      id: `fooditem_${item.fooditem_id}`,
      name: `${item.fooditem_name} (food item)`,
      type: 'fooditem',
      originalId: item.fooditem_id
    })
  })

  return sources
})

// Load data
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

const loadIngredients = async () => {
  loadingIngredients.value = true
  try {
    const response = await fetch(`${API_BASE}/ingredients`)
    const data = await response.json()
    rawIngredients.value = data.ingredients || []
  } catch (err) {
    console.error('Failed to load ingredients:', err)
  } finally {
    loadingIngredients.value = false
  }
}

const loadUnitTypes = async () => {
  loadingUnitTypes.value = true
  try {
    const response = await fetch(`${API_BASE}/unit-types`)
    const data = await response.json()
    unitTypes.value = data.unit_types || []
  } catch (err) {
    console.error('Failed to load unit types:', err)
  } finally {
    loadingUnitTypes.value = false
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

// Ingredient management
const addIngredient = () => {
  ingredients.value.push({
    source: null,
    ri_quantity: null,
    ri_unit_type_id: null
  })
}

const removeIngredient = (index) => {
  if (ingredients.value.length > 1) {
    ingredients.value.splice(index, 1)
  }
}

const openCreateIngredientDialog = (index) => {
  currentIngredientIndex.value = index
  showCreateIngredientDialog.value = true
}

const createIngredient = async () => {
  if (!newIngredient.value.ingredient_name) return

  creatingIngredient.value = true
  try {
    const response = await fetch(`${API_BASE}/ingredients`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newIngredient.value)
    })

    if (!response.ok) throw new Error('Failed to create ingredient')

    const created = await response.json()

    // Add to list
    rawIngredients.value.push(created)

    // Select it for current ingredient
    if (currentIngredientIndex.value !== null) {
      ingredients.value[currentIngredientIndex.value].source = {
        id: `ingredient_${created.ingredient_id}`,
        name: `${created.ingredient_name} (ingredient)`,
        type: 'ingredient',
        originalId: created.ingredient_id
      }
    }

    // Reset and close
    newIngredient.value = { ingredient_name: '', ingredient_description: '' }
    showCreateIngredientDialog.value = false
    currentIngredientIndex.value = null
  } catch (err) {
    console.error('Failed to create ingredient:', err)
    alert('Failed to create ingredient')
  } finally {
    creatingIngredient.value = false
  }
}

// Food item creation
const createFoodItem = async () => {
  if (!newFoodItem.value.fooditem_name) return

  creatingFoodItem.value = true
  try {
    const response = await fetch(`${API_BASE}/food-items`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newFoodItem.value)
    })

    if (!response.ok) throw new Error('Failed to create food item')

    const created = await response.json()

    // Add to list
    foodItems.value.push(created)

    // Select it
    formData.value.fooditem_id = created.fooditem_id

    // Reset and close
    newFoodItem.value = { fooditem_name: '', fooditem_description: '' }
    showCreateFoodItemDialog.value = false
  } catch (err) {
    console.error('Failed to create food item:', err)
    alert('Failed to create food item')
  } finally {
    creatingFoodItem.value = false
  }
}

// Instruction management
const addInstruction = () => {
  instructions.value.push({
    step_number: instructions.value.length + 1,
    instruction_text: ''
  })
}

const removeInstruction = (index) => {
  if (instructions.value.length > 1) {
    instructions.value.splice(index, 1)
    // Renumber steps
    instructions.value.forEach((inst, idx) => {
      inst.step_number = idx + 1
    })
  }
}

// Form submission
const handleSubmit = async () => {
  const { valid } = await formRef.value.validate()
  if (!valid) return

  // Build recipe data
  const recipeData = {
    ...formData.value,
    ingredients: ingredients.value.map(ing => ({
      ri_ingredient_id: ing.source?.type === 'ingredient' ? ing.source.originalId : null,
      ri_fooditem_id: ing.source?.type === 'fooditem' ? ing.source.originalId : null,
      ri_quantity: ing.ri_quantity,
      ri_unit_type_id: ing.ri_unit_type_id
    })),
    instructions: instructions.value
  }

  emit('submit', recipeData)
}

onMounted(() => {
  loadFoodItems()
  loadIngredients()
  loadUnitTypes()
  loadCategories()
})

// Watch for initialData changes (handles async loading)
watch(() => props.initialData, (newData) => {
  if (newData) {
    formData.value = {
      name: newData.name || '',
      description: newData.description || '',
      fooditem_id: newData.fooditem_id || null,
      category_id: newData.category_id || []
    }

    // Update ingredients from the new data
    if (newData.ingredients && Array.isArray(newData.ingredients)) {
      ingredients.value = newData.ingredients.map(ing => {
        if (ing.ri_ingredient_id) {
          return {
            source: {
              id: `ingredient_${ing.ri_ingredient_id}`,
              name: `${ing.ingredient_name || 'Unknown'} (ingredient)`,
              type: 'ingredient',
              originalId: ing.ri_ingredient_id
            },
            ri_quantity: ing.ri_quantity,
            ri_unit_type_id: ing.ri_unit_type_id
          }
        } else if (ing.ri_fooditem_id) {
          return {
            source: {
              id: `fooditem_${ing.ri_fooditem_id}`,
              name: `${ing.fooditem_name || 'Unknown'} (food item)`,
              type: 'fooditem',
              originalId: ing.ri_fooditem_id
            },
            ri_quantity: ing.ri_quantity,
            ri_unit_type_id: ing.ri_unit_type_id
          }
        }
        return {
          source: null,
          ri_quantity: ing.ri_quantity || null,
          ri_unit_type_id: ing.ri_unit_type_id || null
        }
      })
    }

    // Update instructions from the new data
    if (newData.instructions && Array.isArray(newData.instructions)) {
      instructions.value = newData.instructions.map(inst => ({
        step_number: inst.step_number,
        instruction_text: inst.instruction_text || ''
      }))
    }
  }
}, { immediate: true })
</script>

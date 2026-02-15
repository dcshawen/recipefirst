<template>
  <div v-if="active.item" class="page-container max-w-4xl">
    <div class="card">
      <!-- Action Buttons -->
      <div class="flex justify-end gap-2 p-4 border-b border-gray-100">
        <button class="btn btn-primary btn-sm" @click="navigateToEdit">
          <i class="mdi mdi-pencil"></i> Edit
        </button>
        <button class="btn btn-danger btn-sm" @click="showDeleteDialog = true">
          <i class="mdi mdi-delete"></i> Delete
        </button>
      </div>

      <div class="p-5 space-y-4">
        <div v-for="col in active.columns" :key="col.field">
          <span v-if="col === active.columns[0]" class="block text-2xl font-bold text-gray-900">{{ active.item[col.field] }}</span>
          <div v-else>
            <span class="form-label">{{ col.label }}</span>
            <template v-if="Array.isArray(active.item[col.field])">
              <!-- Special handling for instructions -->
              <template v-if="col.field.toLowerCase() === 'instructions'">
                <ol class="ml-6 space-y-1 text-sm text-gray-700">
                  <li v-for="(instruction, idx) in active.item[col.field]" :key="idx" class="leading-relaxed">
                    {{ instruction }}
                  </li>
                </ol>
              </template>
              <!-- Special handling for categories -->
              <template v-else-if="col.field.toLowerCase() === 'categories'">
                <div v-if="Array.isArray(active.item[col.field])" class="flex flex-wrap gap-1 mt-1">
                  <span v-for="cat in active.item[col.field]" :key="typeof cat === 'object' ? (cat.category_name || cat.name) : cat" class="chip">
                    {{ typeof cat === 'object' ? (cat.category_name || cat.name) : cat }}
                  </span>
                </div>
                <span v-else class="text-sm text-gray-700">{{ active.item[col.field] }}</span>
              </template>
              <!-- Special handling for recipes -->
              <template v-else-if="col.field.toLowerCase() === 'recipes'">
                <ul class="list-disc ml-6 text-sm">
                  <li v-for="(recipe, idx) in active.item[col.field]" :key="idx">
                    <a
                      @click="goToRecipe(recipe.recipe_id)"
                      class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium"
                    >
                      {{ recipe.recipe_name }}
                    </a>
                    <span v-if="recipe.recipe_description" class="text-gray-500 ml-2">
                      — {{ recipe.recipe_description }}
                    </span>
                  </li>
                </ul>
              </template>
              <!-- Special handling for ingredients -->
              <template v-else-if="col.field.toLowerCase() === 'ingredients'">
                <ul class="list-disc ml-6 text-sm">
                  <li v-for="(ingredient, idx) in active.item[col.field]" :key="idx">
                    <span class="text-gray-700">{{ ingredient.ri_quantity }} {{ ingredient.unit_type }}&nbsp;</span>
                    <a
                      v-if="ingredient.ri_ingredient_id && ingredient.ingredient_name"
                      @click="goToIngredient(ingredient.ri_ingredient_id)"
                      class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium"
                    >
                      {{ ingredient.ingredient_name }}
                    </a>
                    <a
                      v-else-if="ingredient.ri_fooditem_id && ingredient.fooditem_name"
                      @click="goToFoodItem(ingredient.ri_fooditem_id)"
                      class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium"
                    >
                      {{ ingredient.fooditem_name }}
                    </a>
                    <span v-else class="text-gray-700">{{ ingredient.ingredient_name || ingredient.fooditem_name || 'Unknown' }}</span>
                  </li>
                </ul>
              </template>
              <!-- Special handling for fooditems -->
              <template v-else-if="col.field.toLowerCase() === 'fooditems'">
                <ul class="list-disc ml-6 text-sm">
                  <li v-for="(fooditem, idx) in active.item[col.field]" :key="idx">
                    <a
                      @click="goToFoodItem(fooditem.fooditem_id)"
                      class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium"
                    >
                      {{ fooditem.fooditem_name }}
                    </a>
                    <span v-if="fooditem.fooditem_description" class="text-gray-500 ml-2">
                      — {{ fooditem.fooditem_description }}
                    </span>
                  </li>
                </ul>
              </template>
              <!-- Regular list display -->
              <template v-else>
                <ul class="list-disc ml-6 text-sm text-gray-700">
                  <li v-for="(entry, idx) in active.item[col.field]" :key="idx">
                    <template v-if="typeof entry === 'object' && entry !== null">
                      <ul class="list-disc ml-6">
                        <li v-for="(val, key) in entry" :key="key">
                          <span class="font-semibold text-gray-600">{{ key }}:</span>
                          <template v-if="Array.isArray(val)">
                            <ul class="list-disc ml-6">
                              <li v-for="(subval, subidx) in val" :key="subidx">
                                <span v-if="typeof subval === 'object' && subval !== null">
                                  <ul class="list-disc ml-6">
                                    <li v-for="(subsubval, subkey) in subval" :key="subkey">
                                      <span class="font-semibold text-gray-600">{{ subkey }}:</span> {{ subsubval }}
                                    </li>
                                  </ul>
                                </span>
                                <span v-else>{{ subval }}</span>
                              </li>
                            </ul>
                          </template>
                          <template v-else-if="typeof val === 'object' && val !== null">
                            <ul class="list-disc ml-6">
                              <li v-for="(subval, subkey) in val" :key="subkey">
                                <span class="font-semibold text-gray-600">{{ subkey }}:</span> {{ subval }}
                              </li>
                            </ul>
                          </template>
                          <template v-else> {{ val }}</template>
                        </li>
                      </ul>
                    </template>
                    <template v-else>{{ entry }}</template>
                  </li>
                </ul>
              </template>
            </template>
            <template v-else-if="typeof active.item[col.field] === 'object' && active.item[col.field] !== null">
              <!-- Handle single recipe object -->
              <template v-if="col.field === 'recipe' && active.item[col.field] && active.item[col.field].recipe_name">
                <a
                  @click="goToRecipe(active.item[col.field].recipe_id)"
                  class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium text-sm"
                >
                  {{ active.item[col.field].recipe_name }}
                </a>
              </template>
              <!-- Default object handling -->
              <template v-else>
                <ul class="list-disc ml-6 text-sm text-gray-700">
                  <li v-for="(val, key) in active.item[col.field]" :key="key">
                    <span class="font-semibold text-gray-600">{{ key }}:</span>
                    <template v-if="Array.isArray(val)">
                      <ul class="list-disc ml-6">
                        <li v-for="(subval, subidx) in val" :key="subidx">
                          <span v-if="typeof subval === 'object' && subval !== null">
                            <ul class="list-disc ml-6">
                              <li v-for="(subsubval, subkey) in subval" :key="subkey">
                                <span class="font-semibold text-gray-600">{{ subkey }}:</span> {{ subsubval }}
                              </li>
                            </ul>
                          </span>
                          <span v-else>{{ subval }}</span>
                        </li>
                      </ul>
                    </template>
                    <template v-else-if="typeof val === 'object' && val !== null">
                      <ul class="list-disc ml-6">
                        <li v-for="(subval, subkey) in val" :key="subkey">
                          <span class="font-semibold text-gray-600">{{ subkey }}:</span> {{ subval }}
                        </li>
                      </ul>
                    </template>
                    <template v-else> {{ val }}</template>
                  </li>
                </ul>
              </template>
            </template>
            <template v-else>
              <!-- Handle reference fields (ending with _id) -->
              <template v-if="isReferenceField(col.field) && active.item[col.field]">
                <a
                  v-if="resolvedReferences[col.field]"
                  @click="goToReference(col.field, active.item[col.field])"
                  class="text-brand-600 hover:text-brand-800 cursor-pointer hover:underline font-medium text-sm"
                >
                  {{ resolvedReferences[col.field] }}
                </a>
                <span v-else class="text-sm text-gray-400">{{ active.item[col.field] }}</span>
              </template>
              <template v-else>
                <span class="text-sm text-gray-700">{{ active.item[col.field] }}</span>
              </template>
            </template>
          </div>
        </div>

        <!-- Associated Recipes for Food Items -->
        <div v-if="associatedRecipes.length" class="border-t border-gray-100 pt-4">
          <h3 class="section-title">Recipes Using This Item</h3>
          <ul class="divide-y divide-gray-100">
            <li v-for="r in associatedRecipes" :key="r.id" class="py-3 flex justify-between items-center">
              <span class="font-medium text-sm text-gray-900">{{ r.name || r.title }}</span>
              <button @click="goToRecipe(r.id)" class="btn btn-outline btn-sm">View Recipe</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteDialog" class="modal-backdrop" @click="showDeleteDialog = false"></div>
    <div v-if="showDeleteDialog" class="modal">
      <div class="modal-content">
        <div class="bg-danger-600 text-white px-6 py-4 rounded-t-xl">
          <h3 class="text-lg font-semibold">Confirm Deletion</h3>
        </div>
        <div class="px-6 py-5">
          <p class="mb-2 text-sm text-gray-700">Are you sure you want to delete this item?</p>
          <p class="text-sm text-danger-700 font-semibold">Warning: This action cannot be undone.</p>
        </div>
        <div class="flex justify-end gap-2 px-6 py-4 border-t border-gray-100">
          <button class="btn btn-ghost" @click="showDeleteDialog = false">Cancel</button>
          <button class="btn btn-danger" @click="confirmDelete" :disabled="deleting">
            {{ deleting ? 'Deleting...' : 'Delete' }}
          </button>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="loading-overlay">
    <div class="spinner"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useNavigation } from '../composables/useNavigation.js'

const props = defineProps({
  itemData: {
    type: Object,
    required: false,
    default: () => ({ item: null, columns: [] })
  },
  id: {
    type: String,
    required: false
  }
})

const route = useRoute()
const router = useRouter()
const API_BASE = import.meta.env.VITE_API_BASE || '/api'

// Import the parseItemData and fetchJSON function from our composable
const { parseItemData, fetchJSON } = useNavigation()

const active = ref({ item: props.itemData?.item || null, columns: props.itemData?.columns || [] })
const associatedRecipes = ref([])
const resolvedReferences = ref({})
const showDeleteDialog = ref(false)
const deleting = ref(false)

function getColumns(obj) {
  return Object.keys(obj).map(key => ({
    field: key,
    label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
  }))
}

function resolveTypeToApiPrefix() {
  const path = route.path
  if (path.startsWith('/ingredients')) return 'ingredients'
  if (path.startsWith('/recipes')) return 'recipes'
  if (path.startsWith('/meals')) return 'meals'
  if (path.startsWith('/fooditems')) return 'food-items' // note API hyphen
  return null
}

async function load() {
  const id = route.params.id
  const prefix = resolveTypeToApiPrefix()
  if (!prefix || !id) return

  try {
    const rawItem = await fetchJSON(`/${prefix}/${id}`)
    
    // Preserve original nested objects and arrays that should remain as entities
    const originalRecipe = rawItem.recipe
    const originalRecipes = rawItem.recipes
    const originalFooditems = rawItem.fooditems
    const originalIngredients = rawItem.ingredients
    const originalCategories = rawItem.categories
    
    // Process the item data using our composable's parseItemData function
    const processedData = parseItemData({ item: rawItem })
    const processedItem = processedData.item
    
    // Restore the original nested data if it was there
    if (originalRecipe) {
      processedItem.recipe = originalRecipe
    }
    if (originalRecipes) {
      processedItem.recipes = originalRecipes
    }
    if (originalFooditems) {
      processedItem.fooditems = originalFooditems
    }
    if (originalIngredients) {
      processedItem.ingredients = originalIngredients
    }
    if (originalCategories) {
      processedItem.categories = originalCategories
    }
    
    active.value = { item: processedItem, columns: getColumns(processedItem).slice(1) }

    // Resolve reference fields to their display names
    resolvedReferences.value = await resolveReferences(processedItem)

    // If food item, fetch associated recipes
    if (prefix === 'food-items') {
      const r = await fetchJSON(`/${prefix}/${id}/recipes`)
      associatedRecipes.value = Array.isArray(r?.recipes) ? r.recipes : []
    } else {
      associatedRecipes.value = []
    }
  } catch (e) {
    console.error('Failed to load item', e)
  }
}

function goToRecipe(id) {
  router.push(`/recipes/${id}`)
}

function goToFoodItem(id) {
  router.push(`/fooditems/${id}`)
}

function goToIngredient(id) {
  router.push(`/ingredients/${id}`)
}

// Navigate to edit page
function navigateToEdit() {
  const id = route.params.id
  const prefix = resolveTypeToApiPrefix()

  if (!prefix || !id) {
    console.error('Cannot determine entity type or ID for editing')
    return
  }

  // Map frontend routes to edit routes
  const routeMap = {
    'ingredients': '/ingredients',
    'recipes': '/recipes',
    'meals': '/meals',
    'food-items': '/fooditems',
    'unit-types': '/unittypes',
    'categories': '/categories'
  }

  const basePath = routeMap[prefix] || `/${prefix}`
  router.push(`${basePath}/${id}/edit`)
}

// Delete the current item
async function confirmDelete() {
  deleting.value = true
  const id = route.params.id
  const prefix = resolveTypeToApiPrefix()

  if (!prefix || !id) {
    console.error('Cannot determine entity type or ID for deletion')
    deleting.value = false
    return
  }

  try {
    const response = await fetch(`${API_BASE}/${prefix}/${id}`, {
      method: 'DELETE'
    })

    if (!response.ok) {
      throw new Error(`Delete failed with status ${response.status}`)
    }

    // Close dialog
    showDeleteDialog.value = false

    // Navigate back to the list view
    const listPath = `/${prefix === 'food-items' ? 'fooditems' : prefix}`
    router.push(listPath)
  } catch (error) {
    console.error('Failed to delete item:', error)
    alert('Failed to delete item. Please try again.')
  } finally {
    deleting.value = false
  }
}

// Check if a field is a reference field (ends with _id)
function isReferenceField(fieldName) {
  return fieldName.endsWith('_id') && fieldName !== 'recipe_id' && fieldName !== 'ingredient_id' && fieldName !== 'fooditem_id' && fieldName !== 'meal_id'
}

// Check if an object represents an entity (has id and name fields)
function isEntityObject(obj) {
  if (!obj || typeof obj !== 'object') return false
  const keys = Object.keys(obj)
  const hasId = keys.some(key => key.endsWith('_id'))
  const hasName = keys.some(key => key.includes('name'))
  return hasId && hasName
}

// Get the API endpoint for a reference field
function getReferenceEndpoint(fieldName) {
  const fieldMap = {
    'recipe_fooditem_id': 'food-items',
    'ri_fooditem_id': 'food-items',
    'ri_ingredient_id': 'ingredients',
    'mf_fooditem_id': 'food-items',
    'recipe_id': 'recipes',
    'fooditem_id': 'food-items',
    'ingredient_id': 'ingredients',
    'meal_id': 'meals',
    'category_id': 'categories'
  }
  return fieldMap[fieldName] || null
}

// Get the route path for a reference field
function getReferencePath(fieldName) {
  const pathMap = {
    'recipe_fooditem_id': 'fooditems',
    'ri_fooditem_id': 'fooditems',
    'ri_ingredient_id': 'ingredients',
    'mf_fooditem_id': 'fooditems',
    'recipe_id': 'recipes',
    'fooditem_id': 'fooditems',
    'ingredient_id': 'ingredients',
    'meal_id': 'meals',
    'category_id': 'categories'
  }
  return pathMap[fieldName] || null
}

// Navigate to a referenced item
function goToReference(fieldName, id) {
  const path = getReferencePath(fieldName)
  if (path) {
    router.push(`/${path}/${id}`)
  }
}

// Resolve reference fields to their display names
async function resolveReferences(item) {
  const resolved = {}
  
  for (const [fieldName, value] of Object.entries(item)) {
    if (isReferenceField(fieldName) && value) {
      const endpoint = getReferenceEndpoint(fieldName)
      if (endpoint) {
        try {
          const referencedItem = await fetchJSON(`/${endpoint}/${value}`)
          // Try to find a name field in the referenced item
          const nameField = Object.keys(referencedItem).find(key => key.includes('name'))
          if (nameField) {
            resolved[fieldName] = referencedItem[nameField]
          }
        } catch (e) {
          console.warn(`Failed to resolve reference ${fieldName}:`, e)
        }
      }
    }
  }
  
  return resolved
}

onMounted(async () => {
  // If we didn't receive item via props (e.g., direct navigation), fetch it
  if (!active.value.item) {
    load()
  } else {
    // If we have item data from props, preserve original nested objects and resolve references
    const originalData = props.itemData?.item
    if (originalData?.recipe) {
      active.value.item.recipe = originalData.recipe
    }
    if (originalData?.recipes) {
      active.value.item.recipes = originalData.recipes
    }
    if (originalData?.fooditems) {
      active.value.item.fooditems = originalData.fooditems
    }
    if (originalData?.ingredients) {
      active.value.item.ingredients = originalData.ingredients
    }
    if (originalData?.categories) {
      active.value.item.categories = originalData.categories
    }
    resolvedReferences.value = await resolveReferences(active.value.item)
  }
})

watch(() => route.fullPath, () => {
  load()
})
</script>


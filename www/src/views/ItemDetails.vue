<template>
  <div v-if="active.item" class="p-4 m-6 bg-gray-100 rounded h-fit w-[90%]">
    <div class="pb-3" v-for="col in active.columns" :key="col.field">
      <span v-if="col === active.columns[0]" class="font-bold text-2xl">{{ active.item[col.field] }}</span>
      <span v-else>
        <span class="font-semibold">{{ col.label }}: </span>
        <template v-if="Array.isArray(active.item[col.field])">
          <!-- Special handling for instructions (should show as numbered list without bullets) -->
          <template v-if="col.field.toLowerCase() === 'instructions'">
            <ol class="ml-6 space-y-1">
              <li v-for="(instruction, idx) in active.item[col.field]" :key="idx" class="leading-relaxed">
                {{ instruction }}
              </li>
            </ol>
          </template>
          <!-- Special handling for categories (show as comma-separated list) -->
          <template v-else-if="col.field.toLowerCase() === 'categories'">
            <span v-if="Array.isArray(active.item[col.field])">
              {{ active.item[col.field].map(cat => typeof cat === 'object' ? (cat.category_name || cat.name) : cat).join(', ') }}
            </span>
            <span v-else>{{ active.item[col.field] }}</span>
          </template>
          <!-- Special handling for recipes (show as links to each recipe) -->
          <template v-else-if="col.field.toLowerCase() === 'recipes'">
            <ul class="list-disc ml-6">
              <li v-for="(recipe, idx) in active.item[col.field]" :key="idx">
                <a 
                  @click="goToRecipe(recipe.recipe_id)"
                  class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
                >
                  {{ recipe.recipe_name }}
                </a>
                <span v-if="recipe.recipe_description" class="text-gray-600 ml-2">
                  - {{ recipe.recipe_description }}
                </span>
              </li>
            </ul>
          </template>
          <!-- Special handling for ingredients (show with clickable ingredient names) -->
          <template v-else-if="col.field.toLowerCase() === 'ingredients'">
            <ul class="list-disc ml-6">
              <li v-for="(ingredient, idx) in active.item[col.field]" :key="idx">
                <span>{{ ingredient.ri_quantity }} {{ ingredient.unit_type }}&nbsp;</span>
                <a 
                  v-if="ingredient.ri_ingredient_id && ingredient.ingredient_name"
                  @click="goToIngredient(ingredient.ri_ingredient_id)"
                  class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
                >
                  {{ ingredient.ingredient_name }}
                </a>
                <a 
                  v-else-if="ingredient.ri_fooditem_id && ingredient.fooditem_name"
                  @click="goToFoodItem(ingredient.ri_fooditem_id)"
                  class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
                >
                  {{ ingredient.fooditem_name }}
                </a>
                <span v-else>{{ ingredient.ingredient_name || ingredient.fooditem_name || 'Unknown' }}</span>
              </li>
            </ul>
          </template>
          <!-- Special handling for fooditems (show as links to each food item) -->
          <template v-else-if="col.field.toLowerCase() === 'fooditems'">
            <ul class="list-disc ml-6">
              <li v-for="(fooditem, idx) in active.item[col.field]" :key="idx">
                <a 
                  @click="goToFoodItem(fooditem.fooditem_id)"
                  class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
                >
                  {{ fooditem.fooditem_name }}
                </a>
                <span v-if="fooditem.fooditem_description" class="text-gray-600 ml-2">
                  - {{ fooditem.fooditem_description }}
                </span>
              </li>
            </ul>
          </template>
          <!-- Regular list display for ingredients and other arrays -->
          <template v-else>
            <ul class="list-disc ml-6">
              <li v-for="(entry, idx) in active.item[col.field]" :key="idx">
                <template v-if="typeof entry === 'object' && entry !== null">
                  <ul class="list-disc ml-6">
                    <li v-for="(val, key) in entry" :key="key">
                      <span class="font-semibold">{{ key }}:</span>
                      <template v-if="Array.isArray(val)">
                        <ul class="list-disc ml-6">
                          <li v-for="(subval, subidx) in val" :key="subidx">
                            <span v-if="typeof subval === 'object' && subval !== null">
                              <ul class="list-disc ml-6">
                                <li v-for="(subsubval, subkey) in subval" :key="subkey">
                                  <span class="font-semibold">{{ subkey }}:</span> {{ subsubval }}
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
                            <span class="font-semibold">{{ subkey }}:</span> {{ subval }}
                          </li>
                        </ul>
                      </template>
                      <template v-else>
                        {{ val }}
                      </template>
                    </li>
                  </ul>
                </template>
                <template v-else>
                  {{ entry }}
                </template>
              </li>
            </ul>
          </template>
        </template>
        <template v-else-if="typeof active.item[col.field] === 'object' && active.item[col.field] !== null">
          <!-- Handle single recipe object for backward compatibility -->
          <template v-if="col.field === 'recipe' && active.item[col.field] && active.item[col.field].recipe_name">
            <a 
              @click="goToRecipe(active.item[col.field].recipe_id)"
              class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
            >
              {{ active.item[col.field].recipe_name }}
            </a>
          </template>
          <!-- Default object handling -->
          <template v-else>
            <ul class="list-disc ml-6">
              <li v-for="(val, key) in active.item[col.field]" :key="key">
                <span class="font-semibold">{{ key }}:</span>
                <template v-if="Array.isArray(val)">
                  <ul class="list-disc ml-6">
                    <li v-for="(subval, subidx) in val" :key="subidx">
                      <span v-if="typeof subval === 'object' && subval !== null">
                        <ul class="list-disc ml-6">
                          <li v-for="(subsubval, subkey) in subval" :key="subkey">
                            <span class="font-semibold">{{ subkey }}:</span> {{ subsubval }}
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
                      <span class="font-semibold">{{ subkey }}:</span> {{ subval }}
                    </li>
                  </ul>
                </template>
                <template v-else>
                  {{ val }}
                </template>
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
              class="text-blue-600 hover:text-blue-800 cursor-pointer underline"
            >
              {{ resolvedReferences[col.field] }}
            </a>
            <span v-else class="text-gray-500">{{ active.item[col.field] }}</span>
          </template>
          <template v-else>
            {{ active.item[col.field] }}
          </template>
        </template>
      </span>
    </div>

    <!-- Associated Recipes for Food Items -->
    <div v-if="associatedRecipes.length" class="mt-6 border-t pt-4">
      <h3 class="text-lg font-semibold mb-3">Recipes Using This Item</h3>
      <ul class="divide-y">
        <li v-for="r in associatedRecipes" :key="r.id" class="py-2 flex justify-between items-center">
          <span class="font-medium">{{ r.name || r.title }}</span>
          <button @click="goToRecipe(r.id)" class="px-3 py-1 bg-blue-600 text-white rounded text-sm hover:bg-blue-700">View Recipe</button>
        </li>
      </ul>
    </div>
  </div>
  <div v-else class="p-4 m-6">Loading…</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useNavigation } from '../composables/useNavigation.js'

const props = defineProps({
  itemData: {
    type: Object,
    required: true
  }
})

const route = useRoute()
const router = useRouter()
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

// Import the parseItemData function from our composable
const { parseItemData } = useNavigation()

const active = ref({ item: props.itemData?.item || null, columns: props.itemData?.columns || [] })
const associatedRecipes = ref([])
const resolvedReferences = ref({})

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

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`)
  return res.json()
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

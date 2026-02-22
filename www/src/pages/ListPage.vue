<template>
  <div class="w-[92vw] sm:w-[50vw] mx-auto mt-8">
    <div class="relative pt-4 sm:pt-12">
      <button
        class="absolute top-4 right-4 z-10 hidden sm:flex items-center gap-2 bg-blue-600 text-white px-3 py-2 rounded-md shadow hover:bg-blue-700 transition-colors"
        @click="navigateToCreate"
      >
        <i class="mdi mdi-plus"></i>
        <span>Add New</span>
      </button>
    <GenericList v-if="config" :config="config" />
    <div v-else class="p-4 text-red-600">Unknown list: {{ entity }}</div>
		</div>
    
    <button
      class="fixed bottom-20 right-4 w-14 h-14 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 flex items-center justify-center text-2xl transition-colors sm:hidden"
      @click="navigateToCreate"
    >
      <i class="mdi mdi-plus" />
    </button>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import GenericList from '../components/GenericList.vue'

const props = defineProps({
  entity: {
    type: String,
    required: true
  }
})

const router = useRouter()
const entity = computed(() => props.entity)

const configs = {
  ingredients: {
    endpoint: '/ingredients',
    dataKey: 'ingredients',
    idField: 'ingredient_id',
    routePrefix: 'ingredients',
    columns: [
      { key: 'name', label: 'Ingredient', field: 'ingredient_name', type: 'link' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  },
  recipes: {
    endpoint: '/recipes',
    dataKey: 'recipes',
    idField: 'recipe_id',
    routePrefix: 'recipes',
    columns: [
      { key: 'name', label: 'Recipe Name', field: 'recipe_name', type: 'link' },
      { key: 'category', label: 'Category', field: 'categories', type: 'categories' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  },
  meals: {
    endpoint: '/meals',
    dataKey: 'meals',
    idField: 'meal_id',
    routePrefix: 'meals',
    columns: [
      { key: 'name', label: 'Meal Name', field: 'meal_name', type: 'link' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  },
  fooditems: {
    endpoint: '/food-items',
    dataKey: 'food_items',
    idField: 'fooditem_id',
    routePrefix: 'fooditems',
    columns: [
      { key: 'name', label: 'Food Item Name', field: 'fooditem_name', type: 'link' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  },
  unittypes: {
    endpoint: '/unit-types',
    dataKey: 'unit_types',
    idField: 'id',
    routePrefix: 'unittypes',
    columns: [
      { key: 'type', label: 'Unit Type', field: 'unit_type', type: 'text' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  },
  categories: {
    endpoint: '/categories',
    dataKey: 'categories',
    idField: 'category_id',
    routePrefix: 'categories',
    columns: [
      { key: 'name', label: 'Category Name', field: 'category_name', type: 'text' },
      { key: 'updated', label: 'Last Updated', field: 'updated_at', type: 'date' }
    ]
  }
}

const config = computed(() => configs[entity.value])

const navigateToCreate = () => {
  const prefix = config.value?.routePrefix || entity.value
  router.push(`/${prefix}/create`)
}
</script>

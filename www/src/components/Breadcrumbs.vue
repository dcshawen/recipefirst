<template>
  <nav v-if="breadcrumbs.length" class="flex items-center gap-1 text-sm text-gray-500">
    <template v-for="(item, index) in breadcrumbs" :key="index">
      <span v-if="index > 0" class="mx-1">›</span>
      <router-link v-if="item.to && !item.disabled" :to="item.to" class="text-brand-600 hover:text-brand-800 hover:underline">
        {{ item.title }}
      </router-link>
      <span v-else class="text-gray-800 font-medium">{{ item.title }}</span>
    </template>
  </nav>
</template>

<script setup>
import { computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useBreadcrumbs } from '../composables/useBreadcrumbs'

const route = useRoute()
const { dynamicTitle, setDynamicTitle } = useBreadcrumbs()

// Clear the title when changing base routes to prevent stale titles
watch(() => route.path, (newPath, oldPath) => {
  // If navigating away from an item to a different base entity or to a list
  if (newPath.split('/')[1] !== oldPath.split('/')[1] || newPath.split('/').length < 3) {
    setDynamicTitle('')
  }
})

const entityMap = {
  ingredients: { label: 'Pantry', listPath: '/pantry' },
  fooditems: { label: 'Pantry', listPath: '/pantry' },
  pantry: { label: 'Pantry', listPath: '/pantry' },
  recipes: { label: 'Recipes', listPath: '/recipes' },
  meals: { label: 'Meals', listPath: '/meals' },
  unittypes: { label: 'Unit Types', listPath: '/unittypes' },
  categories: { label: 'Categories', listPath: '/categories' }
}

const breadcrumbs = computed(() => {
  const path = route.path
  if (path === '/') return []

  const segments = path.split('/').filter(Boolean)
  if (segments.length === 0) return []

  const crumbs = [{ title: 'Home', to: '/' }]
  const entityKey = segments[0]
  const entityEntry = entityMap[entityKey]
  const entityNamePlural = entityEntry ? entityEntry.label : (entityKey.charAt(0).toUpperCase() + entityKey.slice(1))
  const entityListPath = entityEntry ? entityEntry.listPath : `/${entityKey}`
  
  let entityNameSingular = entityNamePlural
  if (entityKey === 'categories') entityNameSingular = 'Category'
  else if (entityKey === 'unittypes') entityNameSingular = 'Unit Type'
  else if (entityNamePlural.endsWith('s')) entityNameSingular = entityNamePlural.slice(0, -1)

  crumbs.push({
    title: entityNamePlural,
    to: entityListPath,
    disabled: segments.length === 1
  })

  if (segments.length >= 2) {
    if (segments[1] === 'create') {
      crumbs.push({ title: `Create New`, disabled: true })
    } else {
      const id = segments[1]
      const title = dynamicTitle.value || `${entityNameSingular} #${id}`
      
      if (segments.length >= 3 && segments[2] === 'edit') {
        crumbs.push({ title: `Edit ${title}`, disabled: true })
      } else {
        crumbs.push({ title: title, disabled: true })
      }
    }
  }

  return crumbs
})
</script>

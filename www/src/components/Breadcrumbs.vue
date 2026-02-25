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
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const entityMap = {
  ingredients: 'Ingredients',
  recipes: 'Recipes',
  meals: 'Meals',
  fooditems: 'Food Items',
  unittypes: 'Unit Types',
  categories: 'Categories'
}

const breadcrumbs = computed(() => {
  const path = route.path
  if (path === '/') return []

  const segments = path.split('/').filter(Boolean)
  if (segments.length === 0) return []

  const crumbs = [{ title: 'Home', to: '/' }]
  const entityKey = segments[0]
  const entityNamePlural = entityMap[entityKey] || (entityKey.charAt(0).toUpperCase() + entityKey.slice(1))
  
  let entityNameSingular = entityNamePlural
  if (entityKey === 'categories') entityNameSingular = 'Category'
  else if (entityNamePlural.endsWith('s')) entityNameSingular = entityNamePlural.slice(0, -1)

  crumbs.push({
    title: entityNamePlural,
    to: `/${entityKey}`,
    disabled: segments.length === 1
  })

  if (segments.length >= 2) {
    if (segments[1] === 'create') {
      crumbs.push({ title: `Create New`, disabled: true })
    } else {
      const id = segments[1]
      if (segments.length >= 3 && segments[2] === 'edit') {
        crumbs.push({ title: `Edit ${entityNameSingular} #${id}`, disabled: true })
      } else {
        crumbs.push({ title: `${entityNameSingular} #${id}`, disabled: true })
      }
    }
  }

  return crumbs
})
</script>

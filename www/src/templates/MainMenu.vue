<template>
  <nav class="flex flex-col h-full" aria-label="Main navigation">
    <!-- Brand area on mobile (shown inside sidebar) -->
    <div class="flex items-center gap-2 px-5 pt-5 pb-3 lg:pt-6">
      <i class="mdi mdi-chef-hat text-brand-600 text-xl lg:hidden"></i>
      <span class="text-sm font-semibold text-gray-400 uppercase tracking-wider">Navigation</span>
    </div>

    <ul class="flex-1 px-3 space-y-0.5">
      <li v-for="item in menuItems" :key="item.path">
        <button
          class="w-full flex items-center gap-3 px-3 py-2.5 text-sm rounded-lg transition-all duration-150"
          :class="isActive(item.path)
            ? 'bg-brand-50 text-brand-700 font-semibold shadow-sm'
            : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'"
          @click="navigate(item.path)"
        >
          <i :class="['mdi', item.icon, 'text-lg', isActive(item.path) ? 'text-brand-600' : 'text-gray-400']"></i>
          <span>{{ item.text }}</span>
        </button>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const emit = defineEmits(['updateItemData', 'updateLoading', 'navigate'])

const router = useRouter()
const route = useRoute()

const menuItems = [
  { text: 'Home',        path: '/',             icon: 'mdi-home-outline' },
  { text: 'Recipes',     path: '/recipes',      icon: 'mdi-food' },
  { text: 'Meals',       path: '/meals',        icon: 'mdi-silverware-fork-knife' },
  { text: 'Food Items',  path: '/fooditems',    icon: 'mdi-food-apple-outline' },
  { text: 'Ingredients', path: '/ingredients',  icon: 'mdi-grain' },
  { text: 'Categories',  path: '/categories',   icon: 'mdi-tag-outline' },
  { text: 'Units',       path: '/unittypes',    icon: 'mdi-scale-balance' },
]

function isActive(path) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}

function navigate(path) {
  router.push(path)
  emit('navigate')
}
</script>
import { createRouter, createWebHistory } from 'vue-router'
import ListView from './components/ListView.vue'

const routes = [
  { path: '/', component: ListView, props: { source: 'ingredients' } },
  { path: '/recipes', component: ListView, props: { source: 'recipes' } },
  { path: '/ingredients', component: ListView, props: { source: 'ingredients' } },
  { path: '/components', component: ListView, props: { source: 'components' } },
  { path: '/meals', component: ListView, props: { source: 'meals' } },
  { path: '/units', component: ListView, props: { source: 'units' } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
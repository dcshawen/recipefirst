import { createRouter, createWebHistory } from 'vue-router'
import ListView from './components/ListView.vue'

const routes = [
  { path: '/', component: { template: '<div>Home</div>' } },
  { path: '/recipes', component: { template: '<div>Recipes (coming soon)</div>' } },
  { path: '/ingredients', component: ListView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
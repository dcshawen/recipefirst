import { createRouter, createWebHistory } from 'vue-router'
import ListView from './components/ListView.vue'
import { createListResource } from './modules/list-resource.js'

// Helper to generate ListView routes
function listViewRoute({
  path,
  source,
  title,
  titleField,
  descField,
  keyField,
}) {
  return {
    path,
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource(source)
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title,
      titleField,
      descField,
      keyField,
      source,
      items: route.meta.items || [],
    }),
  }
}

const routes = [
  listViewRoute({
    path: '/',
    source: 'ingredients',
    title: 'Ingredients',
    titleField: 'ingredient_name',
    descField: 'ingredient_description',
    keyField: 'ingredient_id',
  }),
  listViewRoute({
    path: '/recipes',
    source: 'recipes',
    title: 'Recipes',
    titleField: 'recipe_name',
    descField: 'recipe_description',
    keyField: 'recipe_id',
  }),
  listViewRoute({
    path: '/ingredients',
    source: 'ingredients',
    title: 'Ingredients',
    titleField: 'ingredient_name',
    descField: 'ingredient_description',
    keyField: 'ingredient_id',
  }),
  listViewRoute({
    path: '/components',
    source: 'components',
    title: 'Components',
    titleField: 'component_name',
    descField: 'component_description',
    keyField: 'component_id',
  }),
  listViewRoute({
    path: '/meals',
    source: 'meals',
    title: 'Meals',
    titleField: 'meal_name',
    descField: 'meal_description',
    keyField: 'meal_id',
  }),
  listViewRoute({
    path: '/units',
    source: 'units',
    title: 'Units',
    titleField: 'unit_name',
    keyField: 'unit_id',
  }),
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
import { createRouter, createWebHistory } from 'vue-router'
import ListView from './components/ListView.vue'
import { createListResource } from './list-resource.js'

const routes = [
  {
    path: '/',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('ingredients')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Ingredients',
      titleField: 'ingredient_name',
      descField: 'ingredient_description',
      keyField: 'ingredient_id',
      source: 'ingredients',
      items: route.meta.items || [],
    }),
  },
  {
    path: '/recipes',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('recipes')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Recipes',
      titleField: 'recipe_name',
      descField: 'recipe_description',
      keyField: 'recipe_id',
      source: 'recipes',
      items: route.meta.items || [],
    }),
  },
  {
    path: '/ingredients',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('ingredients')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Ingredients',
      titleField: 'ingredient_name',
      descField: 'ingredient_description',
      keyField: 'ingredient_id',
      source: 'ingredients',
      items: route.meta.items || [],
    }),
  },
  {
    path: '/components',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('components')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Components',
      titleField: 'component_name',
      descField: 'component_description',
      keyField: 'component_id',
      source: 'components',
      items: route.meta.items || [],
    }),
  },
  {
    path: '/meals',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('meals')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Meals',
      titleField: 'meal_name',
      descField: 'meal_description',
      keyField: 'meal_id',
      source: 'meals',
      items: route.meta.items || [],
    }),
  },
  {
    path: '/units',
    component: ListView,
    beforeEnter: async (to, from, next) => {
      try {
        to.meta.items = await createListResource('units')
        next()
      } catch (e) {
        next(false)
      }
    },
    props: (route) => ({
      title: 'Units',
      titleField: 'unit_name',
      keyField: 'unit_id',
      source: 'units',
      items: route.meta.items || [],
    }),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
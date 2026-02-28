import { createRouter, createWebHistory } from 'vue-router';
import ItemDetails from './views/ItemDetails.vue';
import GenericListView from './views/GenericListView.vue';
import Home from './pages/Home.vue';
import Login from './pages/Login.vue';

import ListPage from './pages/ListPage.vue';

import CreateIngredient from './pages/CreateIngredient.vue';
import CreateFoodItem from './pages/CreateFoodItem.vue';
import CreateUnitType from './pages/CreateUnitType.vue';
import CreateCategory from './pages/CreateCategory.vue';
import CreateRecipe from './pages/CreateRecipe.vue';
import CreateMeal from './pages/CreateMeal.vue';

import EditIngredient from './pages/EditIngredient.vue';
import EditFoodItem from './pages/EditFoodItem.vue';
import EditUnitType from './pages/EditUnitType.vue';
import EditCategory from './pages/EditCategory.vue';
import EditRecipe from './pages/EditRecipe.vue';
import EditMeal from './pages/EditMeal.vue';

const TOKEN_KEY = 'recipefirst_token'

const routes = [
	// Public route – no auth required
	{ path: '/login', component: Login },

	// Protected routes
	{ path: '/', component: Home, meta: { requiresAuth: true } },
	{ path: '/ingredients', component: ListPage, props: { entity: 'ingredients' }, meta: { requiresAuth: true } },
	{ path: '/ingredients/create', component: CreateIngredient, meta: { requiresAuth: true } },
	{ path: '/ingredients/:id/edit', component: EditIngredient, meta: { requiresAuth: true } },
	{ path: '/recipes', component: ListPage, props: { entity: 'recipes' }, meta: { requiresAuth: true } },
	{ path: '/recipes/create', component: CreateRecipe, meta: { requiresAuth: true } },
	{ path: '/recipes/:id/edit', component: EditRecipe, meta: { requiresAuth: true } },
	{ path: '/meals', component: ListPage, props: { entity: 'meals' }, meta: { requiresAuth: true } },
	{ path: '/meals/create', component: CreateMeal, meta: { requiresAuth: true } },
	{ path: '/meals/:id/edit', component: EditMeal, meta: { requiresAuth: true } },
	{ path: '/fooditems', component: ListPage, props: { entity: 'fooditems' }, meta: { requiresAuth: true } },
	{ path: '/fooditems/create', component: CreateFoodItem, meta: { requiresAuth: true } },
	{ path: '/fooditems/:id/edit', component: EditFoodItem, meta: { requiresAuth: true } },
	{ path: '/unittypes', component: ListPage, props: { entity: 'unittypes' }, meta: { requiresAuth: true } },
	{ path: '/unittypes/create', component: CreateUnitType, meta: { requiresAuth: true } },
	{ path: '/unittypes/:id/edit', component: EditUnitType, meta: { requiresAuth: true } },
	{ path: '/categories', component: ListPage, props: { entity: 'categories' }, meta: { requiresAuth: true } },
	{ path: '/categories/create', component: CreateCategory, meta: { requiresAuth: true } },
	{ path: '/categories/:id/edit', component: EditCategory, meta: { requiresAuth: true } },
	{ path: '/ingredients/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } },
	{ path: '/recipes/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } },
	{ path: '/meals/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } },
	{ path: '/fooditems/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } },
	{ path: '/unittypes/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } },
	{ path: '/categories/:id', component: ItemDetails, props: true, meta: { requiresAuth: true } }
];

const router = createRouter({
	history: createWebHistory(),
	routes
});

// Navigation guard – protect routes that require authentication.
//
// Reads the token directly from localStorage so the guard is self-contained
// and does not rely on Vue composition API outside of a component context.
router.beforeEach((to) => {
	const isAuthenticated = !!localStorage.getItem(TOKEN_KEY);

	// Redirect unauthenticated users to /login, preserving the intended path.
	if (to.meta.requiresAuth && !isAuthenticated) {
		return { path: '/login', query: { redirect: to.fullPath } };
	}

	// Prevent authenticated users from reaching the login page.
	if (to.path === '/login' && isAuthenticated) {
		return { path: '/' };
	}
});

export default router;
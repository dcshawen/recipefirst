import { createRouter, createWebHistory } from 'vue-router';
import ItemDetails from './views/ItemDetails.vue';
import GenericListView from './views/GenericListView.vue';
import Home from './pages/Home.vue';

import IngredientList from './pages/IngredientList.vue';
import RecipeList from './pages/RecipeList.vue';
import MealList from './pages/MealList.vue';
import FoodItemList from './pages/FoodItemList.vue';
import UnitTypeList from './pages/UnitTypeList.vue';
import CategoryList from './pages/CategoryList.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/ingredients', component: IngredientList },
    { path: '/recipes', component: RecipeList },
    { path: '/meals', component: MealList },
    { path: '/fooditems', component: FoodItemList },
    { path: '/unittypes', component: UnitTypeList },
    { path: '/categories', component: CategoryList },
    { path: '/ingredients/:id', component: ItemDetails, props: true },
		{ path: '/recipes/:id', component: ItemDetails, props: true },
		{ path: '/meals/:id', component: ItemDetails, props: true },
		{ path: '/fooditems/:id', component: ItemDetails, props: true },
		{ path: '/unittypes/:id', component: ItemDetails, props: true },
		{ path: '/categories/:id', component: ItemDetails, props: true }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
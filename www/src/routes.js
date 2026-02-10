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

const routes = [
    { path: '/', component: Home },
    { path: '/ingredients', component: IngredientList },
    { path: '/ingredients/create', component: CreateIngredient },
    { path: '/ingredients/:id/edit', component: EditIngredient },
    { path: '/recipes', component: RecipeList },
    { path: '/recipes/create', component: CreateRecipe },
    { path: '/recipes/:id/edit', component: EditRecipe },
    { path: '/meals', component: MealList },
    { path: '/meals/create', component: CreateMeal },
    { path: '/meals/:id/edit', component: EditMeal },
    { path: '/fooditems', component: FoodItemList },
    { path: '/fooditems/create', component: CreateFoodItem },
    { path: '/fooditems/:id/edit', component: EditFoodItem },
    { path: '/unittypes', component: UnitTypeList },
    { path: '/unittypes/create', component: CreateUnitType },
    { path: '/unittypes/:id/edit', component: EditUnitType },
    { path: '/categories', component: CategoryList },
    { path: '/categories/create', component: CreateCategory },
    { path: '/categories/:id/edit', component: EditCategory },
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
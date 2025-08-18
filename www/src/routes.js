import { createRouter, createWebHistory } from 'vue-router';
import ItemDetails from './views/ItemDetails.vue';
import GenericListView from './views/GenericListView.vue';
import Home from './pages/Home.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/ingredients', component: GenericListView, props: { type: 'ingredients', linkactive: true } },
    { path: '/recipes', component: GenericListView, props: { type: 'recipes', linkactive: true } },
    { path: '/meals', component: GenericListView, props: { type: 'meals', linkactive: true } },
    { path: '/fooditems', component: GenericListView, props: { type: 'fooditems', linkactive: true } },
    { path: '/unittypes', component: GenericListView, props: { type: 'unit types', linkactive: false } },
    { path: '/categories', component: GenericListView, props: { type: 'categories', linkactive: false } },
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
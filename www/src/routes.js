import { createRouter, createWebHistory } from 'vue-router';
import ItemDetails from './pages/ItemDetails.vue';
import GenericListView from './views/GenericListView.vue';

const routes = [
    { path: '/', component: GenericListView, props: true },
    { path: '/ingredients', component: GenericListView, props: { type: 'ingredients' } },
    { path: '/recipes', component: GenericListView, props: { type: 'recipes' } },
    { path: '/meals', component: GenericListView, props: { type: 'meals' } },
    { path: '/fooditems', component: GenericListView, props: { type: 'fooditems' } },
    { path: '/ingredients/:id', component: ItemDetails, props: true },
		{ path: '/recipes/:id', component: ItemDetails, props: true },
		{ path: '/meals/:id', component: ItemDetails, props: true },
		{ path: '/fooditems/:id', component: ItemDetails, props: true }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
import { createRouter, createWebHistory } from 'vue-router';
import ItemDetails from './pages/ItemDetails.vue';
import GenericListView from './views/GenericListView.vue';

const routes = [
    { path: '/', component: GenericListView, props: true },
    { path: '/ingredients/:id', component: ItemDetails, props: true },
		{ path: '/recipes/:id', component: ItemDetails, props: true },
		{ path: '/meals/:id', component: ItemDetails, props: true }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
	{
		path: '/',
		component: () => import('../views/GenericListView.vue'),
		props: true
	},
	{
		path: '/ingredients/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	},
	{
		path: '/recipes/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	},
	{
		path: '/meals/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	},
	{
		path: '/fooditems/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	},
	{
		path: '/unittypes/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	},
	{
		path: '/categories/:id?',
		component: () => import('../views/ItemDetails.vue'),
		props: true
	}
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
});

export default router;
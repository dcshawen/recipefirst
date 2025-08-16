```javascript
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
	{
		path: '/',
		component: () => import('../views/GenericListView.vue'),
		props: true
	},
	{
		path: '/ingredients/:id?',
		component: () => import('../pages/ItemDetails.vue'),
		props: true
	},
	{
		path: '/recipes/:id?',
		component: () => import('../pages/ItemDetails.vue'),
		props: true
	},
	{
		path: '/meals/:id?',
		component: () => import('../pages/ItemDetails.vue'),
		props: true
	}
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
});

export default router;
```
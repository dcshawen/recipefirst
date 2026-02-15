<template>
	<nav class="flex flex-col p-2 min-h-screen">
		<div class="pt-10">
			<p class="px-3 py-1 text-xs font-semibold uppercase tracking-wider text-gray-500">Main Menu</p>
			<ul class="mt-1 space-y-0.5">
				<li
					v-for="item in [
						{ text: 'Home', path: '/' },
						{ text: 'Ingredients', path: '/ingredients' },
						{ text: 'Recipes', path: '/recipes' },
						{ text: 'Meals', path: '/meals' },
						{ text: 'Food Items', path: '/fooditems' },
						{ text: 'Units', path: '/unittypes' },
						{ text: 'Categories', path: '/categories' }
					]"
					:key="item.path"
				>
					<button
						class="w-full text-left px-3 py-2 text-sm rounded-md hover:bg-gray-100 transition-colors"
						:class="{ 'bg-blue-50 text-blue-700 font-medium': route.path === item.path }"
						@click="router.push(item.path)"
					>
						{{ item.text }}
					</button>
				</li>
			</ul>
		</div>
	</nav>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
</script>
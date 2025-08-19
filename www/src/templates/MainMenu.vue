<template>
	<nav class="flex flex-col space-y-4 p-2 bg-gray-100 min-h-screen">
<!-- 		<button @click="router.push('/')">Home</button>
		<button @click="router.push('/ingredients')">Ingredient Details</button>
		<button @click="router.push('/recipes')">Recipe Details</button>
		<button @click="router.push('/meals')">Meal Details</button>
		<button @click="router.push('/fooditems')">Food Item Details</button>
		<button @click="router.push('/unittypes')">Unit Types</button>
		<button @click="router.push('/categories')">Categories</button> -->

		<v-list
			:lines="false"
			density="compact"
			nav
		>
			<v-list-item
				v-for="item in [
					{ text: 'Home', path: '/' },
					{ text: 'Ingredient Details', path: '/ingredients' },
					{ text: 'Recipe Details', path: '/recipes' },
					{ text: 'Meal Details', path: '/meals' },
					{ text: 'Food Item Details', path: '/fooditems' },
					{ text: 'Unit Types', path: '/unittypes' },
					{ text: 'Categories', path: '/categories' }
				]"
				:key="item.path"
				@click="router.push(item.path)"
			>
				{{ item.text }}
			</v-list-item>
		</v-list>
	</nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

</script>
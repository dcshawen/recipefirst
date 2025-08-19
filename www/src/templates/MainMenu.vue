<template>
	<nav class="flex flex-col space-y-4 p-2 bg-gray-100 w-40 min-h-screen">
		<button @click="router.push('/')">Home</button>
		<button @click="router.push('/ingredients')">Ingredient Details</button>
		<button @click="router.push('/recipes')">Recipe Details</button>
		<button @click="router.push('/meals')">Meal Details</button>
		<button @click="router.push('/fooditems')">Food Item Details</button>
		<button @click="router.push('/unittypes')">Unit Types</button>
		<button @click="router.push('/categories')">Categories</button>
	</nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

</script>
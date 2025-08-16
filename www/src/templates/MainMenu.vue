<template>
	<nav class="flex flex-col space-y-4 p-2 bg-gray-100 w-40 min-h-screen">
		<button @click="$emit('showHome')">Home</button>
		<button @click="$emit('showRandomIngredient')">Ingredient Details</button>
		<button @click="$emit('showRandomRecipe')">Recipe Details</button>
		<button @click="$emit('showRandomMeal')">Meal Details</button>
	</nav>
</template>

<script setup>
// Remove all logic and refs, only emit events
</script>
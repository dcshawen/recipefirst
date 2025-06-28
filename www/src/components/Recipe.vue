<template>
	<div class="recipe">
		<h2 class="text-xl font-semibold">{{ recipe.recipe_name }}</h2>
		<p class="text-gray-600">{{ recipe.recipe_description }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	recipe: {
		type: Object,
		required: true,
	},
});
</script>

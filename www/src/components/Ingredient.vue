<template>
	<div class="ingredient">
		<h2 class="text-xl font-semibold">{{ ingredient.ingredient_name }}</h2>
		<p class="text-gray-600">{{ ingredient.ingredient_description }}</p>
	</div>
</template>

<script setup>
	const props = defineProps({
		ingredient: {
			type: Object,
			required: true,
		},
	});
</script>
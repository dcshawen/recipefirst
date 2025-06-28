<template>
	<div class="meal">
		<h2 class="text-xl font-semibold">{{ meal.meal_name }}</h2>
		<p class="text-gray-600">{{ meal.meal_description }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	meal: {
		type: Object,
		required: true,
	},
});
</script>

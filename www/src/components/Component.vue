<template>
	<div class="component">
		<h2 class="text-xl font-semibold">{{ component.component_name }}</h2>
		<p class="text-gray-600">{{ component.component_description }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	component: {
		type: Object,
		required: true,
	},
});
</script>

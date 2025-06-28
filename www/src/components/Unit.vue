<template>
	<div class="unit">
		<h2 class="text-xl font-semibold">{{ unit.unit_name }}</h2>
	</div>
</template>

<script setup>
const props = defineProps({
	unit: {
		type: Object,
		required: true,
	},
});
</script>

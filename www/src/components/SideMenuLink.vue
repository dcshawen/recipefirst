<template>
	<router-link
		to="/"
		id="side-menu-link"
		class="text-gray-900 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
		>{{ label }}</router-link
	>
</template>

<script setup>
const props = defineProps({
	label: {
		type: String,
	},
	to: {
		type: String,
		default: "/",
	},
});
</script>

<style scoped>
#side-menu-link {
	display: block;
	text-decoration: none;
}
</style>

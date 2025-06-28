<template>
	<div class="list-view-item">
		<h2 class="text-xl font-semibold" v-if="title">{{ title }}</h2>
		<p class="text-gray-600" v-if="desc">{{ desc }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	title: { type: String, required: false },
	desc: { type: String, required: false },
	item: { type: Object, required: true },
	source: { type: String, required: false },
});
</script>

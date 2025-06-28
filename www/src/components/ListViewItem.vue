<template>
	<div class="list-view-item flex w-full p-2 hover:bg-gray-800 cursor-pointer rounded">
		<!-- Title column -->
		<div class="flex-1 flex items-center">
			<h2 class="text-l font-semibold" v-if="title">{{ title }}</h2>
		</div>
		<!-- Description column -->
		<div class="flex-1 flex items-center justify-start">
			<p class="text-gray-600 text-right" v-if="desc">{{ desc }}</p>
		</div>
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

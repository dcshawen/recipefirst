<template>
	<div class="list-view w-full">
		<h1 v-if="title" class="text-2xl font-bold mb-4">{{ title }}</h1>
		<!-- Add column headers if titleField or descField is present -->
		<div v-if="titleField || descField" class="flex font-semibold mb-2 px-15 bg-gray-700 rounded">
			<div v-if="titleField" class="px-2 flex-1 rounded">{{ title.slice(0, -1) }}</div>
			<div v-if="descField" class="px-2 flex-1">Description</div>
		</div>
		<ul class="list-none px-15">
			<li v-for="item in items" :key="itemKey(item)" class="mb-2">
				<ListViewItem 
					:title="titleField ? item[titleField] : undefined"
					:desc="descField ? item[descField] : undefined"
					:item="item"
					:source="source"
				/>
			</li>
		</ul>
	</div>
</template>

<script setup>
import ListViewItem from "./ListViewItem.vue";

const props = defineProps({
	items: { type: Array, default: () => [] },
	title: { type: String, required: false },
	titleField: { type: String, required: false },
	descField: { type: String, required: false },
	keyField: { type: String, required: false },
	source: { type: String, required: false },
});

function itemKey(item) {
	if (props.keyField) return item[props.keyField] || item.id || JSON.stringify(item);
	return item.id || JSON.stringify(item);
}
</script>
<template>
	<li class="ingredient-list-item flex items-center justify-between p-2 border-b">
		<span>
			<span class="ingredient-name font-bold pr-2">{{ ingredient.name }}</span>
			<span class="ingredient-notes text-gray-400 text-[0.5em]">{{ ingredient.description }}</span>
		</span>
		<span class="ingredient-description text-gray-500">{{ ingredient.created_at }}</span>
	</li>
</template>

<script setup>
const props = defineProps({
	ingredient: {
		type: Object,
		required: true
	}
})
</script>

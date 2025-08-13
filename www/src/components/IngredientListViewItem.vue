<template>
	<li class="ingredient-list-item">
		<span class="ingredient-name">{{ ingredient.name }}</span>
		<span class="ingredient-amount">{{ ingredient.amount }}</span>
		<span class="ingredient-unit">{{ ingredient.unit }}</span>
	</li>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
	ingredient: {
		type: Object,
		required: true
	}
})
</script>

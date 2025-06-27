<template>
	<div class="list-view w-full">
		<h1 class="text-2xl font-bold mb-4">Ingredients</h1>
		<ul class="list-none p-0">
			<li v-for="ingredient in ingredients" :key="ingredient.id" class="mb-2">
				<Ingredient :ingredient="ingredient" />
			</li>
		</ul>
	</div>
</template>

<script setup>
	import { ref } from "vue";
	import Ingredient from "./Ingredient.vue";
	import urls from "../assets/urls.json";

	const ingredients = ref([]);
	const apiURL = () => {
		return urls.dev_api.url;
	};

	fetch(`${apiURL()}/ingredients`)
		.then((response) => response.json())
		.then((data) => {
			ingredients.value = data;
		})
		.catch((error) => {
			console.error("Error fetching ingredients:", error);
		})
</script>
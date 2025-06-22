<script setup>
import { ref } from "vue";
import urls from "./assets/urls.json";

const ingredients = ref([]);
const apiURL = () => {
	return urls.dev_api.url;
};

// fetch("http://172.31.63.230:5000/ingredients")
fetch(`${apiURL()}/ingredients`)
	.then((response) => response.json())
	.then((data) => {
		ingredients.value = data;
	})
	.catch((error) => {
		console.error("Error fetching ingredients:", error);
	});
</script>

<template>
	<div class="container">
		<ul>
			<li v-for="ingredient in ingredients" :key="ingredient.ingredient_id">
				{{ ingredient.ingredient_name }}
			</li>
		</ul>
	</div>
</template>

<style scoped></style>

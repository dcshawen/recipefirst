<script setup>
import { ref } from "vue";
import urls from "./assets/urls.json";
import Header from "./components/Header.vue";
import SideMenu from "./components/SideMenu.vue";

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
	<Header />
	<SideMenu />
</template>

<style scoped></style>

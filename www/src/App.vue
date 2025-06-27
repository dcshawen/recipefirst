<script setup>
import { ref } from "vue";
import { RouterLink, createRouter } from "vue-router";
import urls from "./assets/urls.json";
import Header from "./components/Header.vue";
import SideMenu from "./components/SideMenu.vue";
import './routes.js';

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
	});
</script>

<template>
  <div>
		<header>
			<Header />
		</header>
		<div class="flex">
			<SideMenu />
			<RouterView class="pl-25"/>
		</div>
  </div>
</template>

<style scoped></style>

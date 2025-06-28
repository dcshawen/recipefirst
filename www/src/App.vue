<script setup>
import { ref } from "vue";
import { RouterLink, createRouter } from "vue-router";
import urls from "./assets/urls.json";
import Header from "./components/Header.vue";
import SideMenu from "./components/SideMenu.vue";
import './routes.js';
</script>

<template>
  <div>
		<header>
			<Header />
		</header>
		<div class="flex">
			<SideMenu />
			<RouterView class="pl-25 pr-25"/>
		</div>
  </div>
</template>

<style scoped></style>

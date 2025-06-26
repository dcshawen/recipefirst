<template>
	<header class="bg-white shadow">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
			<div class="flex justify-between h-16">
				<div class="flex">
					<nav class="ml-10 flex items-baseline space-x-4">
						<SideMenuLink label="Home" to="/" />
						<SideMenuLink label="Recipes" to="/recipes" />
						<SideMenuLink label="Ingredients" to="/ingredients" />
					</nav>
				</div>
			</div>
		</div>
	</header>
</template>

<script setup>
import SideMenuLink from "./SideMenuLink.vue";
</script>

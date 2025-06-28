<template>
			<div class="flex bg-white w-60 pl-5 h-screen">
				<nav class="mr-10 flex flex-col items-start space-y-4">
					<SideMenuLink label="Home" to="/" />
					<SideMenuLink label="Recipes" to="/recipes" class="hover:bg-orange-900"/>
					<SideMenuLink label="Ingredients" to="/ingredients" />
					<SideMenuLink label="Components" to="/components" />
					<SideMenuLink label="Meals" to="/meals" />
					<SideMenuLink label="Units" to="/units" />
				</nav>
			</div>
			</template>

<script setup>
	import SideMenuLink from "./SideMenuLink.vue";
</script>

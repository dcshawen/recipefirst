<template>
	<div class="list-view w-full">
		<h1 class="text-2xl font-bold mb-4">{{ title }}</h1>
		<ul class="list-none p-0">
			<li v-for="item in items" :key="itemKey(item)" class="mb-2">
				<!-- Render different components or inline for each type -->
				<Ingredient v-if="source === 'ingredients'" :ingredient="item" />
				<div v-else-if="source === 'recipes'">
					<h2 class="text-xl font-semibold">{{ item.recipe_name }}</h2>
					<p class="text-gray-600">{{ item.recipe_description }}</p>
				</div>
				<div v-else-if="source === 'components'">
					<h2 class="text-xl font-semibold">{{ item.component_name }}</h2>
					<p class="text-gray-600">{{ item.component_description }}</p>
				</div>
				<div v-else-if="source === 'units'">
					<h2 class="text-xl font-semibold">{{ item.unit_name }}</h2>
				</div>
				<div v-else-if="source === 'meals'">
					<h2 class="text-xl font-semibold">{{ item.meal_name }}</h2>
					<p class="text-gray-600">{{ item.meal_description }}</p>
				</div>
				<div v-else>
					<pre>{{ item }}</pre>
				</div>
			</li>
		</ul>
	</div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import Ingredient from "./Ingredient.vue";
import urls from "../assets/urls.json";

const props = defineProps({
	source: {
		type: String,
		required: true,
	},
});

const items = ref([]);
const title = ref("");

const endpointMap = {
	ingredients: { url: "/ingredients", title: "Ingredients" },
	recipes: { url: "/recipes", title: "Recipes" },
	components: { url: "/components", title: "Components" },
	units: { url: "/units", title: "Units" },
	meals: { url: "/meals", title: "Meals" },
};

function itemKey(item) {
	if (props.source === "ingredients") return item.ingredient_id || item.id;
	if (props.source === "recipes") return item.recipe_id || item.id;
	if (props.source === "components") return item.component_id || item.id;
	if (props.source === "units") return item.unit_id || item.id;
	if (props.source === "meals") return item.meal_id || item.id;
	return item.id || JSON.stringify(item);
}

function fetchItems() {
	const apiURL = urls.dev_api.url;
	const endpoint = endpointMap[props.source];
	if (!endpoint) {
		items.value = [];
		title.value = "Unknown";
		return;
	}
	title.value = endpoint.title;
	fetch(`${apiURL}${endpoint.url}`)
		.then((response) => response.json())
		.then((data) => {
			items.value = data;
		})
		.catch((error) => {
			console.error(`Error fetching ${props.source}:`, error);
			items.value = [];
		});
}

watch(() => props.source, fetchItems, { immediate: true });
onMounted(fetchItems);
</script>
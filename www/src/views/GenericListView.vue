<template>
	<div class="flex flex-col w-full">
		<h1 class="text-2xl px-2">{{ formattedType }}</h1>
		<div class="flex flex-col w-full my-4">
			<div class="flex bg-gray-100 font-bold">
				<div
					v-for="(column, idx) in itemData.columns"
					:key="idx"
					class="flex-1 px-2 py-2"
				>
					{{ column.label }}
				</div>
			</div>
			<div
				v-for="(item, index) in itemData.items"
				:key="getItemId(item) || index"
				:class="['flex bg-white transition-colors', linkactive ? 'hover:bg-gray-50 cursor-pointer' : '']"
				@click="linkactive && navigateToItem(item)"
			>
				<div
					v-for="(column, idx) in itemData.columns"
					:key="idx"
					class="flex-1 px-2 py-2"
				>
					<template v-if="Array.isArray(item[column.field])">
						{{ item[column.field].join(' ') }}
					</template>
					<template v-else>
						{{ item[column.field] }}
					</template>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "GenericListView",
	props: {
		itemData: {
			type: Object,
			required: true,
		},
		type: {
			type: String,
			default: "Recipe First"
		},
		linkactive: {
			type: Boolean,
			default: false
		}
	},
	methods: {
		navigateToItem(item) {
			// Determine the correct ID field name and value
			const itemId = this.getItemId(item);
			if (itemId === null || itemId === undefined) return;
			
			// Get the base route from current path or type prop
			const baseRoute = this.getBaseRoute();
			if (!baseRoute) return;
			
			// Navigate to the detail route with the actual item ID (no +1 needed)
			const routePath = `/${baseRoute}/${itemId}`;
			this.$router.push(routePath);
		},
		
		getItemId(item) {
			// Try common ID field patterns
			if (item.ingredient_id !== undefined) return item.ingredient_id;
			if (item.recipe_id !== undefined) return item.recipe_id;
			if (item.meal_id !== undefined) return item.meal_id;
			if (item.fooditem_id !== undefined) return item.fooditem_id;
			if (item.category_id !== undefined) return item.category_id;
			if (item.id !== undefined) return item.id; // for unit types
			
			// Fallback: return null if no ID found
			return null;
		},
		
		getBaseRoute() {
			// First try to extract from current route path
			const currentPath = this.$route.path;
			if (currentPath && currentPath !== '/') {
				// Extract the first segment after the slash
				const pathSegments = currentPath.split('/').filter(segment => segment);
				if (pathSegments.length > 0) {
					return pathSegments[0];
				}
			}
			
			// Fallback to type prop if current path doesn't help
			if (this.type && this.type !== "Recipe First") {
				return this.type.toLowerCase().replace(/\s+/g, '').replace(/s$/, 's'); // Keep plural form
			}
			
			// Default fallback
			return null;
		}
	},
	computed: {
		formattedType() {
			if (!this.type) return "Items";
			return this.type.charAt(0).toUpperCase() + this.type.slice(1);
		}
	}
};
</script>

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
				:key="item.id || index"
				class="flex bg-white hover:bg-gray-50 cursor-pointer transition-colors"
				@click="navigateToItem(item.id || index)"
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
		}
	},
	methods: {
		navigateToItem(itemId) {
			if (!itemId) return;
			
			// Get the base route from current path or type prop
			const baseRoute = this.getBaseRoute();
			if (!baseRoute) return;
			
			// Navigate to the detail route with the item ID
			const routePath = `/${baseRoute}/${itemId + 1}`;
			this.$router.push(routePath);
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

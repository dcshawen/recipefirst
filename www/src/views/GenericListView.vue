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
				class="flex bg-white"
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
	computed: {
		formattedType() {
			if (!this.type) return "Items";
			return this.type.charAt(0).toUpperCase() + this.type.slice(1);
		}
	}
};
</script>

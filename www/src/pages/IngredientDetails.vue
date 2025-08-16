<template>
  <div v-if="itemData && itemData.item" class="p-4 m-6 bg-gray-100 rounded">
    <div class="pb-3" v-for="col in itemData.columns" :key="col.field">
			<span v-if="col === itemData.columns[0]" class="font-bold text-2xl">{{ itemData.item[col.field] }}</span>
			<span v-else>
				<span class="font-semibold">{{ col.label }}:</span> {{ itemData.item[col.field] }}
			</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  itemData: {
    type: Object,
    required: true
  }
});
</script>

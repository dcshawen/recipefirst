<template>
  <div v-if="ingredient" class="p-4 m-6 bg-gray-100 rounded">
    <div class="font-bold mb-2">Ingredient Details:</div>
    <div><span class="font-semibold">Name:</span> {{ ingredient.ingredient_name }}</div>
    <div><span class="font-semibold">Description:</span> {{ ingredient.ingredient_description }}</div>
    <div><span class="font-semibold">Notes:</span> {{ ingredient.ingredient_notes }}</div>
    <div><span class="font-semibold">Created On:</span> {{ ingredient.created_at }}</div>
  </div>
</template>

<script setup>
defineProps({
  ingredient: {
    type: Object,
    required: true
  }
});
</script>

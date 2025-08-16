<script setup>
import GenericListView from './views/GenericListView.vue'
import IngredientDetails from './pages/IngredientDetails.vue'
import { ref } from 'vue'
import ingredients from './dev/ingredients.json'

// Start test items
let columns = ref([
    { label: 'Name', field: 'ingredient_name' },
		{ label: 'Description', field: 'ingredient_description' },
    { label: 'Notes', field: 'ingredient_notes' },
    { label: 'Created On', field: 'created_at' },
		{ label: 'Uploaded On', field: 'uploaded_at' }
])

let items = ref(ingredients)

let randomIndex = Math.floor(Math.random() * items.value.length)
let itemData = ref({
	columns: columns.value,
	item: items.value[randomIndex] // single item for details view
})
// End test items
</script>

<template>
    <IngredientDetails :itemData="itemData" />
</template>
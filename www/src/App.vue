<script setup>
import GenericListView from './views/GenericListView.vue'
import IngredientDetails from './pages/IngredientDetails.vue'
import { ref } from 'vue'
import ingredients from './dev/ingredients.json'

// Start test items
let columns = ref([
    { label: 'Name', field: 'ingredient_name' },
    { label: 'Notes', field: 'ingredient_notes' },
    { label: 'Created On', field: 'created_at' }
])

let items = ref(ingredients)

let itemData = ref({
    columns: columns.value,
    items: items.value
})
// End test items
</script>

<template>
    <GenericListView :itemData="itemData" />

    <IngredientDetails :ingredient="items[2]" />
</template>
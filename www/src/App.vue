<script setup>
import GenericListView from './components/GenericListView.vue'
import { ref } from 'vue'

// Start test items
let columns = ref([
    { label: 'Name', field: 'name' },
    { label: 'Description', field: 'description' },
    { label: 'Notes', field: 'notes' },
    { label: 'Created On', field: 'created_at' }
])


let items = ref([
    { id: 1, name: 'Flour', description: "All-purpose flour", notes: "Follow recipe", created_at: new Date().toLocaleDateString() },
    { id: 2, name: 'Sugar', description: "Granulated sugar", notes: "Adjust to taste", created_at: new Date().toLocaleDateString() },
    { id: 3, name: 'Eggs', description: "Large eggs", notes: "Use fresh eggs", created_at: new Date().toLocaleDateString() }
])
let itemData = ref({
    columns: columns.value,
    items: items.value
})
// End test items
</script>

<template>
    <GenericListView :itemData="itemData" />
</template>

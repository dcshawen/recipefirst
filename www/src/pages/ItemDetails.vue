<template>
  <div v-if="active.item" class="p-4 m-6 bg-gray-100 rounded h-fit w-[90%]">
    <div class="pb-3" v-for="col in active.columns" :key="col.field">
      <span v-if="col === active.columns[0]" class="font-bold text-2xl">{{ active.item[col.field] }}</span>
      <span v-else>
        <span class="font-semibold">{{ col.label }}: </span>
        <template v-if="Array.isArray(active.item[col.field])">
          <ul class="list-disc ml-6">
            <li v-for="(entry, idx) in active.item[col.field]" :key="idx">
              <template v-if="typeof entry === 'object' && entry !== null">
                <ul class="list-disc ml-6">
                  <li v-for="(val, key) in entry" :key="key">
                    <span class="font-semibold">{{ key }}:</span>
                    <template v-if="Array.isArray(val)">
                      <ul class="list-disc ml-6">
                        <li v-for="(subval, subidx) in val" :key="subidx">
                          <span v-if="typeof subval === 'object' && subval !== null">
                            <ul class="list-disc ml-6">
                              <li v-for="(subsubval, subkey) in subval" :key="subkey">
                                <span class="font-semibold">{{ subkey }}:</span> {{ subsubval }}
                              </li>
                            </ul>
                          </span>
                          <span v-else>{{ subval }}</span>
                        </li>
                      </ul>
                    </template>
                    <template v-else-if="typeof val === 'object' && val !== null">
                      <ul class="list-disc ml-6">
                        <li v-for="(subval, subkey) in val" :key="subkey">
                          <span class="font-semibold">{{ subkey }}:</span> {{ subval }}
                        </li>
                      </ul>
                    </template>
                    <template v-else>
                      {{ val }}
                    </template>
                  </li>
                </ul>
              </template>
              <template v-else>
                {{ entry }}
              </template>
            </li>
          </ul>
        </template>
        <template v-else-if="typeof active.item[col.field] === 'object' && active.item[col.field] !== null">
          <ul class="list-disc ml-6">
            <li v-for="(val, key) in active.item[col.field]" :key="key">
              <span class="font-semibold">{{ key }}:</span>
              <template v-if="Array.isArray(val)">
                <ul class="list-disc ml-6">
                  <li v-for="(subval, subidx) in val" :key="subidx">
                    <span v-if="typeof subval === 'object' && subval !== null">
                      <ul class="list-disc ml-6">
                        <li v-for="(subsubval, subkey) in subval" :key="subkey">
                          <span class="font-semibold">{{ subkey }}:</span> {{ subsubval }}
                        </li>
                      </ul>
                    </span>
                    <span v-else>{{ subval }}</span>
                  </li>
                </ul>
              </template>
              <template v-else-if="typeof val === 'object' && val !== null">
                <ul class="list-disc ml-6">
                  <li v-for="(subval, subkey) in val" :key="subkey">
                    <span class="font-semibold">{{ subkey }}:</span> {{ subval }}
                  </li>
                </ul>
              </template>
              <template v-else>
                {{ val }}
              </template>
            </li>
          </ul>
        </template>
        <template v-else>
          {{ active.item[col.field] }}
        </template>
      </span>
    </div>

    <!-- Associated Recipes for Food Items -->
    <div v-if="associatedRecipes.length" class="mt-6 border-t pt-4">
      <h3 class="text-lg font-semibold mb-3">Recipes Using This Item</h3>
      <ul class="divide-y">
        <li v-for="r in associatedRecipes" :key="r.id" class="py-2 flex justify-between items-center">
          <span class="font-medium">{{ r.name || r.title }}</span>
          <button @click="goToRecipe(r.id)" class="px-3 py-1 bg-blue-600 text-white rounded text-sm hover:bg-blue-700">View Recipe</button>
        </li>
      </ul>
    </div>
  </div>
  <div v-else class="p-4 m-6">Loading…</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const props = defineProps({
  itemData: {
    type: Object,
    required: true
  }
})

const route = useRoute()
const router = useRouter()
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const active = ref({ item: props.itemData?.item || null, columns: props.itemData?.columns || [] })
const associatedRecipes = ref([])

function getColumns(obj) {
  return Object.keys(obj).map(key => ({
    field: key,
    label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
  }))
}

function resolveTypeToApiPrefix() {
  const path = route.path
  if (path.startsWith('/ingredients')) return 'ingredients'
  if (path.startsWith('/recipes')) return 'recipes'
  if (path.startsWith('/meals')) return 'meals'
  if (path.startsWith('/fooditems')) return 'food-items' // note API hyphen
  return null
}

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`)
  return res.json()
}

async function load() {
  const id = route.params.id
  const prefix = resolveTypeToApiPrefix()
  if (!prefix || !id) return

  try {
    const item = await fetchJSON(`/${prefix}/${id}`)
    active.value = { item, columns: getColumns(item).slice(1) }

    // If food item, fetch associated recipes
    if (prefix === 'food-items') {
      const r = await fetchJSON(`/${prefix}/${id}/recipes`)
      associatedRecipes.value = Array.isArray(r?.recipes) ? r.recipes : []
    } else {
      associatedRecipes.value = []
    }
  } catch (e) {
    console.error('Failed to load item', e)
  }
}

function goToRecipe(id) {
  router.push(`/recipes/${id}`)
}

onMounted(() => {
  // If we didn't receive item via props (e.g., direct navigation), fetch it
  if (!active.value.item) {
    load()
  }
})

watch(() => route.fullPath, () => {
  load()
})
</script>

<template>
  <div v-if="itemData && itemData.item" class="p-4 m-6 bg-gray-100 rounded">
    <div class="pb-3" v-for="col in itemData.columns" :key="col.field">
      <span v-if="col === itemData.columns[0]" class="font-bold text-2xl">{{ itemData.item[col.field] }}</span>
      <span v-else>
        <span class="font-semibold">{{ col.label }}: </span>
        <template v-if="Array.isArray(itemData.item[col.field])">
          <ul class="list-disc ml-6">
            <li v-for="(entry, idx) in itemData.item[col.field]" :key="idx">
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
        <template v-else-if="typeof itemData.item[col.field] === 'object' && itemData.item[col.field] !== null">
          <ul class="list-disc ml-6">
            <li v-for="(val, key) in itemData.item[col.field]" :key="key">
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
          {{ itemData.item[col.field] }}
        </template>
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

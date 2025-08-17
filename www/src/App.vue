<script setup>
import { ref } from 'vue'
import Header from './templates/Header.vue'
import MainMenu from './templates/MainMenu.vue'
import Footer from './templates/Footer.vue'

const itemData = ref({
  item: null,
  columns: []
})
const isLoading = ref(false)

function updateItemData(newData) {
  itemData.value = newData
}

function updateLoading(loading) {
  isLoading.value = loading
}
</script>

<template>
  <Header />
  <div class="flex pb-4">
    <MainMenu 
      class="min-h-screen"
      @updateItemData="updateItemData"
      @updateLoading="updateLoading"
    />
    <router-view
      :itemData="itemData" />
    <div v-if="isLoading" class="loading-overlay">
      <div class="spinner"></div>
    </div>
  </div>
  <Footer class="fixed bottom-0 left-0 w-full" />
</template>

<style>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(255,255,255,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.spinner {
  width: 48px;
  height: 48px;
  border: 6px solid #ccc;
  border-top: 6px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
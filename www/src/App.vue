<script setup>
import { ref, computed, provide } from 'vue'
import { useRoute } from 'vue-router'
import Header from './templates/Header.vue'
import MainMenu from './templates/MainMenu.vue'
import Footer from './templates/Footer.vue'

const route = useRoute()

// Show the full app shell only on authenticated/layout routes.
const showShell = computed(() => route.meta.requiresAuth !== false && route.path !== '/login' && route.path !== '/register')

const itemData = ref({
  item: null,
  columns: []
})
const isLoading = ref(false)
const sidebarOpen = ref(false)

function updateItemData(newData) {
  itemData.value = newData
}

function updateLoading(loading) {
  isLoading.value = loading
}

function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value
}

function closeSidebar() {
  sidebarOpen.value = false
}

provide('sidebarOpen', sidebarOpen)
provide('toggleSidebar', toggleSidebar)
provide('closeSidebar', closeSidebar)
</script>

<template>
  <!-- Public (login) layout -->
  <router-view v-if="!showShell" />

  <!-- Full app shell for authenticated views -->
  <div v-else class="min-h-screen flex flex-col bg-gray-50">
    <Header @toggle-sidebar="toggleSidebar" />

    <div class="flex flex-1 overflow-hidden">
      <!-- Sidebar overlay for mobile -->
      <div
        v-if="sidebarOpen"
        class="fixed inset-0 bg-black/40 z-30 lg:hidden"
        @click="closeSidebar"
      ></div>

      <!-- Sidebar -->
      <aside
        class="fixed top-0 left-0 z-40 h-full w-64 transform transition-transform duration-200 ease-in-out bg-white border-r border-gray-200 lg:static lg:translate-x-0 lg:z-auto"
        :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full'"
      >
        <MainMenu
          @updateItemData="updateItemData"
          @updateLoading="updateLoading"
          @navigate="closeSidebar"
        />
      </aside>

      <!-- Main content -->
      <main class="flex-1 overflow-y-auto pb-16">
        <router-view :itemData="itemData" />
      </main>
    </div>

    <!-- Loading overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="spinner"></div>
    </div>

    <Footer />
  </div>
</template>
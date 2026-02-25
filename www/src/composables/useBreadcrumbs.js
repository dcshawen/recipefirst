import { ref } from 'vue'

const dynamicTitle = ref('')

export function useBreadcrumbs() {
  const setDynamicTitle = (title) => {
    dynamicTitle.value = title
  }
  
  return {
    dynamicTitle,
    setDynamicTitle
  }
}

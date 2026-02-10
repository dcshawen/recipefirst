import { ref, watch } from 'vue'

/**
 * Debounce composable for delaying reactive value updates
 * @param {Ref} value - The reactive value to debounce
 * @param {number} delay - Delay in milliseconds (default: 300)
 * @returns {Ref} debouncedValue - The debounced reactive value
 */
export function useDebounce(value, delay = 300) {
  const debouncedValue = ref(value.value)
  let timeoutId = null

  watch(value, (newValue) => {
    if (timeoutId) {
      clearTimeout(timeoutId)
    }

    timeoutId = setTimeout(() => {
      debouncedValue.value = newValue
    }, delay)
  })

  return debouncedValue
}

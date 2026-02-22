import { ref } from 'vue'
import { useRouter } from 'vue-router'

export function useEntityCreate(entityType, options = {}) {
  const router = useRouter()
  // Use the same API base fallback as other composables: prefer VITE_API_BASE, then '/api'.
  // Avoid using VITE_API_URL here to prevent the dev client from calling loopback
  // (e.g. http://localhost:8000) directly which triggers Private Network Access
  // restrictions when the page is not a secure context.
  const API_BASE = import.meta.env.VITE_API_BASE || '/api'

  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)

  // Config
  const config = {
    apiEndpoint: options.apiEndpoint || `/${entityType}`,
    redirectPath: options.redirectPath || `/${entityType}`,
    idField: options.idField || `${entityType}_id`,
    successMessage: options.successMessage || `${entityType} created successfully!`,
    errorMessage: options.errorMessage || `Failed to create ${entityType}`,
    ...options
  }

  /**
   * Create an entity
   * @param {Object} data - The entity data to create
   * @returns {Promise<Object>} The created entity
   */
  const createEntity = async (data) => {
    loading.value = true
    error.value = null
    success.value = false

    try {
      const url = `${API_BASE}${config.apiEndpoint}`
      console.debug('[useEntityCreate] POST', url, data)

      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })

      const text = await response.text().catch(() => '')
      let result
      try {
        result = text ? JSON.parse(text) : {}
      } catch (e) {
        console.debug('[useEntityCreate] Non-JSON response:', text)
        result = { raw: text }
      }

      if (!response.ok) {
        const errMsg = result.detail || config.errorMessage || response.statusText
        console.debug('[useEntityCreate] Error response', response.status, result)
        throw new Error(errMsg)
      }

      console.debug('[useEntityCreate] Success response', response.status, result)
      success.value = true

      // Call success callback if provided
      if (config.onSuccess) {
        config.onSuccess(result)
      }

      // Navigate to detail page or custom path
      if (config.redirectOnSuccess !== false) {
        const entityId = result[config.idField]
        const redirectPath = config.getRedirectPath
          ? config.getRedirectPath(result)
          : `${config.redirectPath}/${entityId}`

        router.push(redirectPath)
      }

      return result
    } catch (err) {
      error.value = err.message
      success.value = false

      // Call error callback if provided
      if (config.onError) {
        config.onError(err)
      }

      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Reset state
   */
  const reset = () => {
    loading.value = false
    error.value = null
    success.value = false
  }

  /**
   * Navigate back to list
   */
  const cancel = () => {
    router.push(config.redirectPath)
  }

  return {
    loading,
    error,
    success,
    createEntity,
    reset,
    cancel
  }
}

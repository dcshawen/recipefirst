import { ref } from 'vue'
import { useRouter } from 'vue-router'

export function useEntityUpdate(entityType, entityId, options = {}) {
  const router = useRouter()
  const API_BASE = import.meta.env.VITE_API_BASE || '/api'

  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)
  const data = ref(null)

  // Config
  const config = {
    apiEndpoint: options.apiEndpoint || `/${entityType}`,
    redirectPath: options.redirectPath || `/${entityType}`,
    idField: options.idField || `${entityType}_id`,
    successMessage: options.successMessage || `${entityType} updated successfully!`,
    errorMessage: options.errorMessage || `Failed to update ${entityType}`,
    ...options
  }

  /**
   * Fetch existing entity data
   * @returns {Promise<Object>} The entity data
   */
  const fetchEntity = async () => {
    loading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE}${config.apiEndpoint}/${entityId}`)

      if (!response.ok) {
        throw new Error('Failed to fetch entity')
      }

      const result = await response.json()
      data.value = result
      return result
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Update an entity
   * @param {Object} updateData - The updated entity data
   * @returns {Promise<Object>} The updated entity
   */
  const updateEntity = async (updateData) => {
    loading.value = true
    error.value = null
    success.value = false

    try {
      const response = await fetch(`${API_BASE}${config.apiEndpoint}/${entityId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updateData)
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        throw new Error(errorData.detail || config.errorMessage)
      }

      const result = await response.json()
      success.value = true

      // Call success callback if provided
      if (config.onSuccess) {
        config.onSuccess(result)
      }

      // Navigate to detail page or custom path
      if (config.redirectOnSuccess !== false) {
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
   * Navigate back to detail view
   */
  const cancel = () => {
    router.push(`${config.redirectPath}/${entityId}`)
  }

  return {
    loading,
    error,
    success,
    data,
    fetchEntity,
    updateEntity,
    reset,
    cancel
  }
}

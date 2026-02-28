import { ref, computed } from 'vue'

const TOKEN_KEY = 'recipefirst_token'
const API_BASE = () => import.meta.env.VITE_API_BASE || '/api'

// Module-level singleton state so all composable instances share the same reactive refs.
const token = ref(localStorage.getItem(TOKEN_KEY) || null)

/**
 * Auth composable.
 *
 * Exposes:
 *   token         - the raw JWT string (or null)
 *   isAuthenticated - computed boolean
 *   login(credentials) - POST /login, store token, return response
 *   logout()       - clear token from storage and state
 *   getAuthHeaders() - returns { Authorization: 'Bearer <token>' } or {}
 */
export function useAuth() {
	const isAuthenticated = computed(() => !!token.value)

	/**
	 * Persist a token string to localStorage and reactive state.
	 * @param {string} newToken
	 */
	function setToken(newToken) {
		token.value = newToken
		localStorage.setItem(TOKEN_KEY, newToken)
	}

	/**
	 * Remove the token from localStorage and reactive state.
	 */
	function clearToken() {
		token.value = null
		localStorage.removeItem(TOKEN_KEY)
	}

	/**
	 * Authenticate against the API.
	 * @param {{ username: string, password: string }} credentials
	 * @returns {Promise<void>}
	 * @throws {Error} if credentials are invalid or the request fails
	 */
	async function login(credentials) {
		const response = await fetch(`${API_BASE()}/login`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(credentials)
		})

		if (!response.ok) {
			const body = await response.json().catch(() => ({}))
			throw new Error(body.detail || 'Login failed')
		}

		const data = await response.json()
		setToken(data.access_token)
	}

	/**
	 * Clear the session token and log the user out.
	 */
	function logout() {
		clearToken()
	}

	/**
	 * Build an Authorization header object if a token is present.
	 * Pass the result into fetch's `headers` option alongside other headers.
	 * @returns {Record<string, string>}
	 */
	function getAuthHeaders() {
		return token.value ? { Authorization: `Bearer ${token.value}` } : {}
	}

	return {
		token,
		isAuthenticated,
		login,
		logout,
		getAuthHeaders
	}
}

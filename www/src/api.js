/**
 * Centralized API fetch utility.
 *
 * Wraps the native fetch() and automatically attaches the Authorization header
 * when a token is present in localStorage. This is the single place where the
 * header injection logic lives; individual composables should call apiFetch
 * rather than fetch directly.
 */

const TOKEN_KEY = 'recipefirst_token'

/**
 * Drop-in replacement for fetch that injects `Authorization: Bearer <token>`
 * when a token is stored.
 *
 * @param {string} url
 * @param {RequestInit} [options]
 * @returns {Promise<Response>}
 */
export function apiFetch(url, options = {}) {
	const token = localStorage.getItem(TOKEN_KEY)

	const headers = {
		...(options.headers || {}),
		...(token ? { Authorization: `Bearer ${token}` } : {})
	}

	return fetch(url, { ...options, headers })
}

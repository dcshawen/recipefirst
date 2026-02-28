/**
 * Centralized API fetch utility.
 *
 * Wraps the native fetch() and automatically attaches the Authorization header
 * when a token is present in localStorage. This is the single place where the
 * header injection logic lives; individual composables should call apiFetch
 * rather than fetch directly.
 *
 * Global 401 handling: when any response comes back as 401 Unauthorized the
 * stored token is cleared and the user is redirected to /login. The router is
 * imported lazily to avoid a circular-dependency issue (routes.js -> composables
 * -> api.js -> routes.js).
 */

const TOKEN_KEY = 'recipefirst_token'

/**
 * Drop-in replacement for fetch that injects `Authorization: Bearer <token>`
 * when a token is stored and handles 401 responses globally.
 *
 * @param {string} url
 * @param {RequestInit} [options]
 * @returns {Promise<Response>}
 */
export async function apiFetch(url, options = {}) {
	const token = localStorage.getItem(TOKEN_KEY)

	const headers = {
		...(options.headers || {}),
		...(token ? { Authorization: `Bearer ${token}` } : {})
	}

	const response = await fetch(url, { ...options, headers })

	if (response.status === 401) {
		// Clear the invalid/expired token.
		localStorage.removeItem(TOKEN_KEY)

		// Lazily import the router to avoid circular module dependencies.
		const { default: router } = await import('./routes.js')
		const currentPath = router.currentRoute.value.fullPath

		// Only redirect if we are not already on the login page.
		if (router.currentRoute.value.path !== '/login') {
			router.push({ path: '/login', query: { redirect: currentPath } })
		}
	}

	return response
}

/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Enable dark mode based on the 'dark' class on the HTML element
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

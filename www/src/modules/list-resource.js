// list-resource.js
// Utility to fetch list data for a given resource type

import urls from "../assets/urls.json";

const endpointMap = {
  ingredients: "/ingredients",
  recipes: "/recipes",
  components: "/components",
  units: "/units",
  meals: "/meals"
};

export async function createListResource(source) {
  const apiURL = urls.dev_api.url;
  const endpoint = endpointMap[source];
  if (!endpoint) throw new Error(`Unknown source: ${source}`);
  const response = await fetch(`${apiURL}${endpoint}`);
  if (!response.ok) throw new Error(`Failed to fetch ${source}`);
  return await response.json();
}

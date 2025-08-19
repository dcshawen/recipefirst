import { ref } from 'vue'
import { useRouter } from 'vue-router'

// Base URL for API; use /api proxy path for local development to avoid CORS issues
const API_BASE = import.meta.env.VITE_API_BASE || '/api'

export function useNavigation() {
  const router = useRouter()
  const itemData = ref({
    item: null,
    columns: []
  })
  const isLoading = ref(false)

  function getColumns(obj) {
    return Object.keys(obj).map(key => ({
      field: key,
      label: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
    })).slice(1);
  }

  function removeColumns(columns, fieldsToRemove) {
    return columns.filter(col => !fieldsToRemove.includes(col.field))
  }

  function parseItemData(itemData) {
    if (!itemData || typeof itemData !== 'object') return itemData;
    
    const processNestedObjects = (item) => {
      if (!item || typeof item !== 'object' || Array.isArray(item)) return item;
      
      const processedItem = { ...item };
      
      for (const [key, value] of Object.entries(processedItem)) {
        if (Array.isArray(value)) {
          // Special handling for specific recipe fields
          if (key.toLowerCase() === 'ingredients') {
            // Format ingredients as "quantity unit ingredient_name"
            processedItem[key] = value
              .filter(ingredient => ingredient && typeof ingredient === 'object')
              .map(ingredient => {
                const quantity = ingredient.ri_quantity || ingredient.quantity || '';
                const unit = ingredient.unit_type || ingredient.unit || '';
                const name = ingredient.ingredient_name || ingredient.name || '';
                return `${quantity} ${unit} ${name}`.trim();
              })
              .filter(formatted => formatted.length > 0);
          } else if (key.toLowerCase() === 'instructions') {
            // Format instructions as numbered list with just the instruction text
            processedItem[key] = value
              .filter(instruction => instruction && typeof instruction === 'object')
              .sort((a, b) => (a.step_number || 0) - (b.step_number || 0))
              .map((instruction, index) => {
                const text = instruction.instruction_text || instruction.text || instruction.instruction || '';
                return `${index + 1}. ${text}`;
              })
              .filter(formatted => formatted.length > 2); // More than just "1. "
          } else if (key.toLowerCase() === 'categories') {
            // Format categories as simple list of category names
            processedItem[key] = value
              .filter(category => category && typeof category === 'object')
              .map(category => category.category_name || category.name || '')
              .filter(name => name.length > 0);
          } else {
            // Handle other arrays of objects - extract names and join them
            const nameStrings = value
              .filter(v => v && typeof v === 'object')
              .map(obj => {
                const nameProps = Object.keys(obj)
                  .filter(k => k.toLowerCase().includes('name'))
                  .map(k => obj[k])
                  .filter(v => v != null);
                return nameProps.length > 0 ? nameProps[0] : null; // Take first name property
              })
              .filter(name => name != null);
              
            if (nameStrings.length > 0) {
              processedItem[key] = nameStrings.join(', ');
            } else {
              // If no names found, keep original array
              processedItem[key] = value;
            }
          }
        } else if (value && typeof value === 'object') {
          // Handle single nested objects
          const nameProps = Object.keys(value)
            .filter(k => k.toLowerCase().includes('name'))
            .map(k => value[k])
            .filter(v => v != null);
          
          if (nameProps.length > 0) {
            processedItem[key] = nameProps[0]; // Take first name property
          }
        }
      }
      
      return processedItem;
    };

    const result = { ...itemData };
    
    if (Array.isArray(result.items)) {
      result.items = result.items.map(item => processNestedObjects(item));
    } else if (result.item) {
      result.item = processNestedObjects(result.item);
    }
    
    return result;
  }

  async function fetchJSON(path) {
    const res = await fetch(`${API_BASE}${path}`)
    if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`)
    return res.json()
  }

  return {
    router,
    itemData,
    isLoading,
    getColumns,
    removeColumns,
    parseItemData,
    fetchJSON
  }
}

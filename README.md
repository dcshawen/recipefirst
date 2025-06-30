# RecipeFirst

## Advanced Pantry and Recipe Management Software

RecipeFirst is a modern, flexible application for managing your pantry, ingredients, components, and recipes. It is designed for home cooks, meal preppers, and anyone who wants to organize their kitchen and meal planning with precision.

---

## Features

- **Pantry Management:** Track your pantry items, quantities, and units.
- **Ingredient Database:** Store detailed information about each ingredient, including description, notes, and images.
- **Component System:** Build reusable components (like sauces or doughs) from ingredients.
- **Recipe Builder:** Create recipes from components, with full support for quantities and units.
- **Meal Planning:** Organize recipes into meals for advanced planning.
- **Unit Support:** Flexible unit system for all quantities (g, ml, oz, etc.).
- **Relational Database:** Powered by SQLite for robust data integrity and relationships.

---

## Database Schema Overview

- **Units:** List of supported measurement units.
- **Ingredient:** Basic food items with optional description, notes, image, and default unit.
- **Component:** Reusable sub-recipes (e.g., sauces, doughs) made from ingredients.
- **Recipe:** Full recipes, made from components.
- **Meal:** Groupings of recipes for meal planning.
- **RecipeComponent:** Links recipes to their components, with quantity and unit.
- **ComponentIngredient:** Links components to their ingredients, with quantity and unit.

### Example Structure

```
Meal
 └─ Recipe (e.g., Lasagna)
     ├─ Component (e.g., Meat Sauce)
     │    ├─ Ingredient (e.g., Ground Beef)
     │    └─ Ingredient (e.g., Tomato Sauce)
     └─ Component (e.g., Cheese Layer)
          └─ Ingredient (e.g., Ricotta Cheese)
```

---

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/recipefirst.git
   ```
2. **Install dependencies:**
   ```sh
   npm install
   # or
   pnpm install
   ```
3. **Run the app:**
   ```sh
   npm run dev
   ```
4. **Database setup:**
   - The schema is in `recipefirst/schema.sql`.
   - Use SQLite or your preferred DB tool to initialize the database.

---

## Project Structure

- `src/components/` — Vue components (ListView, ListViewItem, etc.)
- `src/routes.js` — App routes
- `recipefirst/schema.sql` — Database schema
- `public/` — Static assets

---

## License

MIT License

---

## Author

[Your Name]

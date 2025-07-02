-- Units (if not already present)
INSERT OR IGNORE INTO Units (unit_id, unit_name) VALUES
(0, 'piece'), (1, 'g'), (2, 'ml'), (3, 'oz'), (4, 'lb'), (5, 'cup'), (6, 'tbsp'), (7, 'tsp'), (8, 'gal');

-- Ingredients
INSERT INTO Ingredient (ingredient_id, ingredient_name, ingredient_description, ingredient_notes, ingredient_image)
VALUES
(1, 'Bread', 'Sliced sandwich bread', '', ''),
(2, 'Cheddar Cheese', 'Mild cheddar cheese', '', ''),
(3, 'Butter', 'Unsalted butter', '', ''),
(4, 'Egg', 'Large chicken egg', '', ''),
(5, 'Milk', 'Whole milk', '', ''),
(6, 'Salt', 'Table salt', '', ''),
(7, 'Pepper', 'Black pepper', '', ''),
(8, 'Tomato', 'Fresh tomato', '', ''),
(9, 'Lettuce', 'Romaine lettuce', '', ''),
(10, 'Chicken Breast', 'Boneless skinless chicken breast', '', ''),
(11, 'Olive Oil', 'Extra virgin olive oil', '', ''),
(12, 'Garlic', 'Fresh garlic cloves', '', ''),
(13, 'Pasta', 'Spaghetti pasta', '', ''),
(14, 'Parmesan Cheese', 'Grated parmesan', '', ''),
(15, 'Basil', 'Fresh basil leaves', '', ''),
(16, 'Ground Beef', '80/20 ground beef', '', ''),
(17, 'Onion', 'Yellow onion', '', ''),
(18, 'Ketchup', 'Tomato ketchup', '', ''),
(19, 'Mustard', 'Yellow mustard', '', ''),
(20, 'Pickle', 'Dill pickle slices', '', ''),
(21, 'Hamburger Bun', 'Classic hamburger bun', '', ''),
(22, 'Mayonnaise', 'Classic mayo', '', ''),
(23, 'Mozzarella Cheese', 'Shredded mozzarella', '', ''),
(24, 'Pizza Dough', 'Prepared pizza dough', '', ''),
(25, 'Marinara Sauce', 'Classic marinara', '', ''),
(26, 'Bell Pepper', 'Red bell pepper', '', ''),
(27, 'Mushroom', 'White button mushroom', '', ''),
(28, 'Spinach', 'Fresh spinach', '', ''),
(29, 'Tortilla', 'Flour tortilla', '', ''),
(30, 'Black Beans', 'Canned black beans', '', '');

-- Components (some are just ingredients, some are prepped mixes)
INSERT INTO Component (component_id, component_name, component_description, component_notes, component_image)
VALUES
(1, 'Grilled Cheese Sandwich', 'Classic grilled cheese', '', ''),
(2, 'Scrambled Eggs', 'Fluffy scrambled eggs', '', ''),
(3, 'Chicken Salad', 'Simple chicken salad', '', ''),
(4, 'Spaghetti Marinara', 'Pasta with marinara sauce', '', ''),
(5, 'Hamburger Patty', 'Seasoned ground beef patty', '', ''),
(6, 'Hamburger', 'Classic hamburger', '', ''),
(7, 'Pizza Margherita', 'Classic pizza with tomato, mozzarella, basil', '', ''),
(8, 'Veggie Pizza', 'Pizza with assorted vegetables', '', ''),
(9, 'Quesadilla', 'Cheese quesadilla', '', ''),
(10, 'Breakfast Burrito', 'Egg and bean breakfast burrito', '', '');

-- Recipes
INSERT INTO Recipe (recipe_id, recipe_name, recipe_description, recipe_notes, recipe_instructions, recipe_servings, recipe_image)
VALUES
(1, 'Grilled Cheese', 'A classic grilled cheese sandwich.', '', 'Butter bread, add cheese, grill until golden.', 1, ''),
(2, 'Scrambled Eggs', 'Fluffy scrambled eggs.', '', 'Whisk eggs, cook in butter, season.', 1, ''),
(3, 'Chicken Salad', 'Simple chicken salad.', '', 'Cook chicken, chop, mix with mayo and veggies.', 2, ''),
(4, 'Spaghetti Marinara', 'Pasta with marinara sauce.', '', 'Cook pasta, heat sauce, combine, top with cheese.', 2, ''),
(5, 'Hamburger', 'Classic hamburger with toppings.', '', 'Grill patty, assemble with bun and toppings.', 1, ''),
(6, 'Pizza Margherita', 'Classic pizza with tomato, mozzarella, basil.', '', 'Top dough, bake at high heat.', 2, ''),
(7, 'Veggie Pizza', 'Pizza with assorted vegetables.', '', 'Top dough with sauce, cheese, veggies, bake.', 2, ''),
(8, 'Quesadilla', 'Cheese quesadilla.', '', 'Fill tortilla with cheese, grill until melted.', 1, ''),
(9, 'Breakfast Burrito', 'Egg and bean breakfast burrito.', '', 'Fill tortilla with eggs, beans, cheese, roll up.', 1, ''),
(10, 'BLT Sandwich', 'Bacon, lettuce, tomato sandwich.', '', 'Layer bacon, lettuce, tomato on bread.', 1, ''),
(11, 'Egg Salad Sandwich', 'Egg salad on bread.', '', 'Mix boiled eggs with mayo, spread on bread.', 1, ''),
(12, 'Chicken Wrap', 'Chicken and veggies in a wrap.', '', 'Fill tortilla with chicken, lettuce, tomato.', 1, ''),
(13, 'Pasta Primavera', 'Pasta with fresh vegetables.', '', 'Cook pasta, sauté veggies, combine.', 2, ''),
(14, 'Cheeseburger', 'Hamburger with cheese.', '', 'Add cheese to patty, assemble burger.', 1, ''),
(15, 'Caprese Salad', 'Tomato, mozzarella, basil salad.', '', 'Layer tomato, mozzarella, basil, drizzle oil.', 2, ''),
(16, 'Garlic Bread', 'Toasted bread with garlic butter.', '', 'Spread garlic butter, toast until golden.', 2, ''),
(17, 'Spinach Omelette', 'Omelette with spinach.', '', 'Cook eggs with spinach, fold and serve.', 1, ''),
(18, 'Chicken Quesadilla', 'Quesadilla with chicken and cheese.', '', 'Fill tortilla with chicken, cheese, grill.', 1, ''),
(19, 'Veggie Burrito', 'Burrito with beans and veggies.', '', 'Fill tortilla with beans, veggies, roll up.', 1, ''),
(20, 'Mushroom Pizza', 'Pizza with mushrooms.', '', 'Top dough with sauce, cheese, mushrooms, bake.', 2, ''),
(21, 'Pepperoni Pizza', 'Pizza with pepperoni.', '', 'Top dough with sauce, cheese, pepperoni, bake.', 2, ''),
(22, 'Chicken Parmesan', 'Breaded chicken with marinara and cheese.', '', 'Bread chicken, fry, top with sauce and cheese, bake.', 2, ''),
(23, 'Tuna Salad', 'Tuna with mayo and veggies.', '', 'Mix tuna with mayo, add veggies.', 2, ''),
(24, 'Egg Fried Rice', 'Rice stir-fried with egg and veggies.', '', 'Cook rice, scramble eggs, stir-fry with veggies.', 2, '');

-- RecipeIngredient (direct ingredient usage in recipes)
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, ri_quantity, unit_id) VALUES
-- Grilled Cheese
(1, 1, 2, 0), -- Bread, 2 pieces
(1, 2, 2, 1), -- Cheddar Cheese, 2g
(1, 3, 1, 6), -- Butter, 1 tbsp
-- Scrambled Eggs
(2, 4, 2, 0), -- Egg, 2 pieces
(2, 5, 30, 2), -- Milk, 30ml
(2, 3, 1, 6), -- Butter, 1 tbsp
(2, 6, 1, 7), -- Salt, 1 tsp
(2, 7, 0.5, 7), -- Pepper, 0.5 tsp
-- Chicken Salad
(3, 10, 1, 0), -- Chicken Breast, 1 piece
(3, 22, 2, 6), -- Mayonnaise, 2 tbsp
(3, 9, 2, 0), -- Lettuce, 2 leaves
(3, 8, 1, 0), -- Tomato, 1 piece
-- Spaghetti Marinara
(4, 13, 100, 1), -- Pasta, 100g
(4, 25, 100, 1), -- Marinara Sauce, 100g
(4, 14, 10, 1), -- Parmesan Cheese, 10g
-- Hamburger
(5, 16, 1, 0), -- Ground Beef, 1 patty
(5, 21, 1, 0), -- Hamburger Bun, 1 piece
(5, 18, 1, 6), -- Ketchup, 1 tbsp
(5, 19, 1, 7), -- Mustard, 1 tsp
(5, 20, 3, 0), -- Pickle, 3 slices
(5, 17, 1, 0), -- Onion, 1 slice
-- Pizza Margherita
(6, 24, 1, 0), -- Pizza Dough, 1 piece
(6, 25, 50, 1), -- Marinara Sauce, 50g
(6, 23, 50, 1), -- Mozzarella Cheese, 50g
(6, 15, 5, 0), -- Basil, 5 leaves
-- Veggie Pizza
(7, 24, 1, 0), -- Pizza Dough, 1 piece
(7, 25, 50, 1), -- Marinara Sauce, 50g
(7, 23, 50, 1), -- Mozzarella Cheese, 50g
(7, 26, 0.5, 0), -- Bell Pepper, 0.5 piece
(7, 27, 3, 0), -- Mushroom, 3 pieces
(7, 28, 20, 1), -- Spinach, 20g
-- Quesadilla
(8, 29, 1, 0), -- Tortilla, 1 piece
(8, 23, 40, 1), -- Mozzarella Cheese, 40g
-- Breakfast Burrito
(9, 29, 1, 0), -- Tortilla, 1 piece
(9, 4, 2, 0), -- Egg, 2 pieces
(9, 30, 50, 1), -- Black Beans, 50g
(9, 23, 20, 1), -- Mozzarella Cheese, 20g
-- BLT Sandwich
(10, 1, 2, 0), -- Bread, 2 pieces
(10, 8, 2, 0), -- Tomato, 2 slices
(10, 9, 2, 0), -- Lettuce, 2 leaves
(10, 3, 1, 6), -- Butter, 1 tbsp
-- Egg Salad Sandwich
(11, 4, 2, 0), -- Egg, 2 pieces
(11, 22, 1, 6), -- Mayonnaise, 1 tbsp
(11, 1, 2, 0), -- Bread, 2 pieces
-- Chicken Wrap
(12, 29, 1, 0), -- Tortilla, 1 piece
(12, 10, 1, 0), -- Chicken Breast, 1 piece
(12, 9, 2, 0), -- Lettuce, 2 leaves
(12, 8, 1, 0), -- Tomato, 1 piece
-- Pasta Primavera
(13, 13, 100, 1), -- Pasta, 100g
(13, 26, 0.5, 0), -- Bell Pepper, 0.5 piece
(13, 28, 20, 1), -- Spinach, 20g
(13, 27, 3, 0), -- Mushroom, 3 pieces
-- Cheeseburger
(14, 16, 1, 0), -- Ground Beef, 1 patty
(14, 21, 1, 0), -- Hamburger Bun, 1 piece
(14, 2, 2, 1), -- Cheddar Cheese, 2g
-- Caprese Salad
(15, 8, 2, 0), -- Tomato, 2 pieces
(15, 23, 40, 1), -- Mozzarella Cheese, 40g
(15, 15, 5, 0), -- Basil, 5 leaves
-- Garlic Bread
(16, 1, 2, 0), -- Bread, 2 pieces
(16, 12, 1, 0), -- Garlic, 1 clove
(16, 3, 1, 6), -- Butter, 1 tbsp
-- Spinach Omelette
(17, 4, 2, 0), -- Egg, 2 pieces
(17, 28, 20, 1), -- Spinach, 20g
(17, 3, 1, 6), -- Butter, 1 tbsp
-- Chicken Quesadilla
(18, 29, 1, 0), -- Tortilla, 1 piece
(18, 10, 1, 0), -- Chicken Breast, 1 piece
(18, 23, 40, 1), -- Mozzarella Cheese, 40g
-- Veggie Burrito
(19, 29, 1, 0), -- Tortilla, 1 piece
(19, 30, 50, 1), -- Black Beans, 50g
(19, 26, 0.5, 0), -- Bell Pepper, 0.5 piece
(19, 28, 20, 1), -- Spinach, 20g
-- Mushroom Pizza
(20, 24, 1, 0), -- Pizza Dough, 1 piece
(20, 25, 50, 1), -- Marinara Sauce, 50g
(20, 23, 50, 1), -- Mozzarella Cheese, 50g
(20, 27, 5, 0), -- Mushroom, 5 pieces
-- Pepperoni Pizza (assume pepperoni is not in ingredient list, skip)
-- Chicken Parmesan
(22, 10, 1, 0), -- Chicken Breast, 1 piece
(22, 25, 50, 1), -- Marinara Sauce, 50g
(22, 23, 40, 1), -- Mozzarella Cheese, 40g
(22, 14, 10, 1); -- Parmesan Cheese, 10g
-- Tuna Salad (assume tuna is not in ingredient list, skip)
-- Egg Fried Rice (assume rice is not in ingredient list, skip)

-- RecipeComponent (for recipes that use components)
INSERT INTO RecipeComponent (recipe_id, component_id, rc_quantity, unit_id) VALUES
(5, 5, 1, 0), -- Hamburger uses Hamburger Patty component
(5, 6, 1, 0), -- Hamburger as a component (for demonstration)
(6, 7, 1, 0), -- Pizza Margherita as a component
(7, 8, 1, 0), -- Veggie Pizza as a component
(8, 9, 1, 0), -- Quesadilla as a component
(9, 10, 1, 0); -- Breakfast Burrito as a component

-- ComponentIngredient (components made from ingredients)
INSERT INTO ComponentIngredient (component_id, ingredient_id, ci_quantity, unit_id) VALUES
(1, 1, 2, 0), -- Grilled Cheese Sandwich: Bread
(1, 2, 2, 1), -- Cheddar Cheese
(1, 3, 1, 6), -- Butter
(2, 4, 2, 0), -- Scrambled Eggs: Egg
(2, 5, 30, 2), -- Milk
(2, 3, 1, 6), -- Butter
(3, 10, 1, 0), -- Chicken Salad: Chicken Breast
(3, 22, 2, 6), -- Mayonnaise
(3, 9, 2, 0), -- Lettuce
(3, 8, 1, 0), -- Tomato
(4, 13, 100, 1), -- Spaghetti Marinara: Pasta
(4, 25, 100, 1), -- Marinara Sauce
(4, 14, 10, 1), -- Parmesan Cheese
(5, 16, 1, 0), -- Hamburger Patty: Ground Beef
(5, 6, 1, 7), -- Salt
(5, 7, 0.5, 7), -- Pepper
(6, 5, 1, 0), -- Hamburger: Hamburger Patty
(6, 21, 1, 0), -- Hamburger Bun
(6, 18, 1, 6), -- Ketchup
(6, 19, 1, 7), -- Mustard
(6, 20, 3, 0), -- Pickle
(6, 17, 1, 0), -- Onion
(7, 24, 1, 0), -- Pizza Margherita: Pizza Dough
(7, 25, 50, 1), -- Marinara Sauce
(7, 23, 50, 1), -- Mozzarella Cheese
(7, 15, 5, 0), -- Basil
(8, 24, 1, 0), -- Veggie Pizza: Pizza Dough
(8, 25, 50, 1), -- Marinara Sauce
(8, 23, 50, 1), -- Mozzarella Cheese
(8, 26, 0.5, 0), -- Bell Pepper
(8, 27, 3, 0), -- Mushroom
(8, 28, 20, 1), -- Spinach
(9, 29, 1, 0), -- Quesadilla: Tortilla
(9, 23, 40, 1), -- Mozzarella Cheese
(10, 29, 1, 0), -- Breakfast Burrito: Tortilla
(10, 4, 2, 0), -- Egg
(10, 30, 50, 1), -- Black Beans
(10, 23, 20, 1); -- Mozzarella Cheese

-- Pantry
INSERT INTO Pantry (pantry_id, pantry_name, pantry_description, pantry_notes)
VALUES
(1, 'Main Pantry', 'Default kitchen pantry', '');

-- PantryComponent (stock some components in the pantry)
INSERT INTO PantryComponent (pantry_id, component_id, pc_quantity, unit_id) VALUES
(1, 1, 2, 0), -- Grilled Cheese Sandwich
(1, 2, 2, 0), -- Scrambled Eggs
(1, 3, 1, 0); -- Chicken Salad

-- Nutrition (minimal, for demonstration)
INSERT INTO Nutrition (nutrition_id, nutrition_calories) VALUES
(1, 300), (2, 250), (3, 400);

-- NutritionIngredient (link some ingredients to nutrition)
INSERT INTO NutritionIngredient (ni_id, ingredient_id, nutrition_id) VALUES
(1, 1, 1), -- Bread
(2, 2, 2), -- Cheddar Cheese
(3, 3, 3); -- Butter

-- NutritionFields (minimal)
INSERT INTO NutritionFields (nutritionfield_id, nutritionfield_name, nutritionfield_value, unit_id) VALUES
(1, 'Calories', '300', NULL),
(2, 'Fat', '10', 1),
(3, 'Protein', '8', 1);

-- Done
-- Done

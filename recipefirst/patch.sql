-- Insert test Ingredients
INSERT INTO Ingredient (ingredient_name, ingredient_description, ingredient_notes, ingredient_image, ingredient_price, unit_id) VALUES
('Ground Beef', 'Lean ground beef, 85/15', 'Store in refrigerator', 'beef.jpg', 6.99, 4),
('Onion', 'Yellow onion, medium size', 'Keep in cool, dry place', 'onion.jpg', 1.25, 4),
('Garlic', 'Fresh garlic cloves', 'Store in pantry', 'garlic.jpg', 0.50, 0),
('Tomato Sauce', 'Canned tomato sauce', 'Check expiration date', 'tomato_sauce.jpg', 1.99, 2),
('Pasta', 'Spaghetti noodles', 'Dry pasta', 'pasta.jpg', 2.49, 1),
('Mozzarella Cheese', 'Shredded mozzarella', 'Keep refrigerated', 'mozzarella.jpg', 4.99, 1),
('Chicken Breast', 'Boneless skinless chicken breast', 'Fresh chicken', 'chicken.jpg', 8.99, 4),
('Rice', 'Long grain white rice', 'Dry rice', 'rice.jpg', 3.99, 1),
('Bell Pepper', 'Red bell pepper', 'Fresh vegetable', 'pepper.jpg', 2.99, 0),
('Olive Oil', 'Extra virgin olive oil', 'Cooking oil', 'olive_oil.jpg', 7.99, 2),
('Salt', 'Table salt', 'Seasoning', 'salt.jpg', 0.99, 1),
('Black Pepper', 'Ground black pepper', 'Spice', 'pepper.jpg', 2.99, 1),
('Bread', 'Whole wheat bread', 'Sliced bread', 'bread.jpg', 3.49, 0),
('Lettuce', 'Iceberg lettuce', 'Fresh lettuce head', 'lettuce.jpg', 1.99, 0),
('Tomato', 'Fresh tomatoes', 'Vine ripened', 'tomato.jpg', 3.99, 4);

-- Insert test Components
INSERT INTO Component (component_name, component_description, component_notes, component_image, component_price, unit_id) VALUES
('Meat Sauce', 'Ground beef tomato sauce', 'Base for pasta dishes', 'meat_sauce.jpg', 8.50, 5),
('Cooked Pasta', 'Boiled spaghetti noodles', 'Al dente pasta', 'cooked_pasta.jpg', 2.00, 5),
('Grilled Chicken', 'Seasoned grilled chicken breast', 'Protein component', 'grilled_chicken.jpg', 12.00, 0),
('Steamed Rice', 'Fluffy white rice', 'Side dish', 'steamed_rice.jpg', 1.50, 5),
('Sautéed Vegetables', 'Mixed bell peppers and onions', 'Vegetable medley', 'sauteed_veg.jpg', 4.00, 5),
('Garlic Bread', 'Toasted bread with garlic butter', 'Side bread', 'garlic_bread.jpg', 3.00, 0),
('Garden Salad', 'Mixed lettuce and tomatoes', 'Fresh salad', 'garden_salad.jpg', 5.00, 0);

-- Insert test Recipes (this will trigger the component creation)
INSERT INTO Recipe (recipe_name, recipe_description, recipe_notes, recipe_instructions, recipe_image) VALUES
('Spaghetti Bolognese', 'Classic Italian pasta dish', 'Family favorite', 'Cook pasta, prepare meat sauce, combine and serve', 'spaghetti_bolognese.jpg'),
('Chicken Rice Bowl', 'Healthy chicken and rice meal', 'High protein meal', 'Grill chicken, steam rice, sauté vegetables, combine', 'chicken_rice_bowl.jpg'),
('Pasta Marinara', 'Simple tomato pasta', 'Vegetarian option', 'Cook pasta, heat sauce, toss together', 'pasta_marinara.jpg');

-- Insert test Meals
INSERT INTO Meal (meal_name, meal_description, meal_notes, meal_image) VALUES
('Weeknight Dinner', 'Quick family dinner', 'Easy to prepare', 'weeknight_dinner.jpg'),
('Sunday Lunch', 'Relaxed weekend meal', 'Take your time', 'sunday_lunch.jpg'),
('Meal Prep Container', 'Portion-controlled meal', 'For meal prepping', 'meal_prep.jpg');

-- Insert RecipeComponent relationships
INSERT INTO RecipeComponent (recipe_id, component_id, rc_quantity, unit_id) VALUES
(1, 1, 2.0, 5),  -- Spaghetti Bolognese uses 2 cups of Meat Sauce
(1, 2, 1.5, 5),  -- Spaghetti Bolognese uses 1.5 cups of Cooked Pasta
(1, 6, 2.0, 0),  -- Spaghetti Bolognese uses 2 pieces of Garlic Bread
(2, 3, 1.0, 0),  -- Chicken Rice Bowl uses 1 piece of Grilled Chicken
(2, 4, 1.0, 5),  -- Chicken Rice Bowl uses 1 cup of Steamed Rice
(2, 5, 0.5, 5),  -- Chicken Rice Bowl uses 0.5 cup of Sautéed Vegetables
(3, 2, 1.0, 5),  -- Pasta Marinara uses 1 cup of Cooked Pasta
(3, 7, 1.0, 0);  -- Pasta Marinara uses 1 Garden Salad

-- Insert ComponentIngredient relationships
INSERT INTO ComponentIngredient (component_id, ingredient_id, ci_quantity, unit_id) VALUES
-- Meat Sauce ingredients
(1, 1, 1.0, 4),   -- 1 lb Ground Beef
(1, 2, 0.5, 0),   -- 0.5 Onion
(1, 3, 3.0, 0),   -- 3 Garlic cloves
(1, 4, 2.0, 5),   -- 2 cups Tomato Sauce
(1, 11, 1.0, 7),  -- 1 tsp Salt
(1, 12, 0.5, 7),  -- 0.5 tsp Black Pepper
-- Cooked Pasta ingredients
(2, 5, 8.0, 3),   -- 8 oz Pasta
(2, 11, 1.0, 7),  -- 1 tsp Salt
-- Grilled Chicken ingredients
(3, 7, 6.0, 3),   -- 6 oz Chicken Breast
(3, 10, 1.0, 6),  -- 1 tbsp Olive Oil
(3, 11, 0.5, 7),  -- 0.5 tsp Salt
(3, 12, 0.25, 7), -- 0.25 tsp Black Pepper
-- Steamed Rice ingredients
(4, 8, 0.5, 5),   -- 0.5 cup Rice
(4, 11, 0.25, 7), -- 0.25 tsp Salt
-- Sautéed Vegetables ingredients
(5, 9, 1.0, 0),   -- 1 Bell Pepper
(5, 2, 0.25, 0),  -- 0.25 Onion
(5, 10, 1.0, 6),  -- 1 tbsp Olive Oil
-- Garlic Bread ingredients
(6, 13, 4.0, 0),  -- 4 pieces Bread
(6, 3, 2.0, 0),   -- 2 Garlic cloves
(6, 10, 2.0, 6),  -- 2 tbsp Olive Oil
-- Garden Salad ingredients
(7, 14, 0.25, 0), -- 0.25 Lettuce head
(7, 15, 0.5, 4);  -- 0.5 lb Tomatoes

-- Insert MealComponent relationships
INSERT INTO MealComponent (meal_id, component_id, mc_quantity, unit_id) VALUES
(1, 1, 1.0, 5),   -- Weeknight Dinner: 1 cup Meat Sauce
(1, 2, 1.0, 5),   -- Weeknight Dinner: 1 cup Cooked Pasta
(1, 7, 1.0, 0),   -- Weeknight Dinner: 1 Garden Salad
(2, 3, 1.0, 0),   -- Sunday Lunch: 1 Grilled Chicken
(2, 4, 1.5, 5),   -- Sunday Lunch: 1.5 cups Steamed Rice
(2, 5, 1.0, 5),   -- Sunday Lunch: 1 cup Sautéed Vegetables
(2, 6, 2.0, 0),   -- Sunday Lunch: 2 pieces Garlic Bread
(3, 3, 1.0, 0),   -- Meal Prep: 1 Grilled Chicken
(3, 4, 1.0, 5),   -- Meal Prep: 1 cup Steamed Rice
(3, 5, 0.75, 5);  -- Meal Prep: 0.75 cup Sautéed Vegetables

-- Insert test Pantry
INSERT INTO Pantry (pantry_name, pantry_description, pantry_notes) VALUES
('Main Pantry', 'Primary kitchen pantry', 'Well-stocked pantry'),
('Backup Storage', 'Additional storage area', 'Overflow items'),
('Spice Cabinet', 'Dedicated spice storage', 'Organized by type');

-- Insert PantryComponent relationships
INSERT INTO PantryComponent (pantry_id, component_id, pc_quantity, unit_id) VALUES
(1, 1, 3.0, 5),   -- Main Pantry: 3 cups Meat Sauce
(1, 2, 2.0, 5),   -- Main Pantry: 2 cups Cooked Pasta
(1, 4, 5.0, 5),   -- Main Pantry: 5 cups Steamed Rice
(2, 3, 2.0, 0),   -- Backup Storage: 2 pieces Grilled Chicken
(2, 6, 6.0, 0),   -- Backup Storage: 6 pieces Garlic Bread
(3, 5, 1.5, 5);   -- Spice Cabinet: 1.5 cups Sautéed Vegetables

-- Insert test Nutrition data
INSERT INTO Nutrition (nutrition_calories) VALUES
(520),  -- Spaghetti Bolognese calories
(380),  -- Chicken Rice Bowl calories
(295),  -- Pasta Marinara calories
(180),  -- Ground Beef per serving
(45),   -- Onion per serving
(25),   -- Garlic per serving
(35),   -- Tomato Sauce per serving
(220),  -- Pasta per serving
(113),  -- Mozzarella per serving
(165);  -- Chicken Breast per serving

-- Insert NutritionIngredient relationships
INSERT INTO NutritionIngredient (ingredient_id, nutrition_id) VALUES
(1, 4),   -- Ground Beef nutrition
(2, 5),   -- Onion nutrition
(3, 6),   -- Garlic nutrition
(4, 7),   -- Tomato Sauce nutrition
(5, 8),   -- Pasta nutrition
(6, 9),   -- Mozzarella nutrition
(7, 10);  -- Chicken Breast nutrition

-- Insert test NutritionFields
INSERT INTO NutritionFields (nutritionfield_name, nutritionfield_value, unit_id) VALUES
('Protein', '25.5', 1),     -- grams
('Carbohydrates', '45.2', 1), -- grams
('Fat', '12.8', 1),         -- grams
('Fiber', '3.2', 1),        -- grams
('Sugar', '8.9', 1),        -- grams
('Sodium', '890', 1),       -- milligrams
('Cholesterol', '75', 1),   -- milligrams
('Vitamin C', '15', 1),     -- milligrams
('Iron', '2.1', 1),         -- milligrams
('Calcium', '120', 1);      -- milligrams

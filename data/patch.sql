/* -- Test data insertion script

-- Insert basic unit types
INSERT OR IGNORE INTO UnitType (unit_type) VALUES
('cup'),
('tablespoon'),
('teaspoon'),
('ounce'),
('pound'),
('gram'),
('kilogram'),
('milliliter'),
('liter'),
('pinch'),
('clove'),
('slice'),
('whole');

-- Insert ingredients
INSERT OR IGNORE INTO Ingredient (ingredient_name) VALUES
('Salt'),
('Black Pepper'),
('Olive Oil'),
('Butter'),
('Garlic'),
('Onion'),
('Flour'),
('Sugar'),
('Brown Sugar'),
('Baking Powder'),
('Baking Soda'),
('Eggs'),
('Milk'),
('Heavy Cream'),
('Chicken Breast'),
('Ground Beef'),
('Bacon'),
('Tomato'),
('Bell Pepper'),
('Carrot'),
('Celery'),
('Potato'),
('Rice'),
('Pasta'),
('Bread'),
('Cheese'),
('Cheddar Cheese'),
('Mozzarella Cheese'),
('Parmesan Cheese'),
('Lemon'),
('Lime'),
('Cilantro'),
('Parsley'),
('Basil'),
('Rosemary'),
('Thyme'),
('Oregano'),
('Cinnamon'),
('Cumin'),
('Paprika'),
('Cayenne Pepper'),
('Nutmeg'),
('Vanilla Extract'),
('Soy Sauce'),
('Honey'),
('Maple Syrup'),
('Vinegar'),
('Red Wine Vinegar'),
('Mustard'),
('Mayonnaise');

-- Insert Food Items
INSERT OR IGNORE INTO FoodItem (fooditem_name, fooditem_description) VALUES
('Grilled Chicken Breast', 'Juicy grilled chicken breast seasoned with herbs'),
('Classic Beef Burger', 'Juicy beef patty with classic toppings'),
('Spaghetti Carbonara', 'Pasta with creamy egg sauce and bacon'),
('Tomato Soup', 'Comforting tomato soup with herbs'),
('Caesar Salad', 'Romaine lettuce with Caesar dressing and croutons'),
('Roasted Vegetables', 'Seasonal vegetables roasted with olive oil'),
('Mashed Potatoes', 'Creamy mashed potatoes with butter'),
('Chocolate Chip Cookies', 'Classic homemade chocolate chip cookies'),
('Blueberry Muffins', 'Fluffy muffins with fresh blueberries'),
('Chicken Stir Fry', 'Chicken and vegetables in a savory sauce'),
('Beef Stew', 'Hearty beef stew with vegetables'),
('Pancakes', 'Fluffy breakfast pancakes'),
('French Toast', 'Classic breakfast french toast'),
('Scrambled Eggs', 'Fluffy scrambled eggs'),
('Grilled Cheese Sandwich', 'Classic comfort food sandwich'),
('Garden Salad', 'Fresh mixed greens with vegetables'),
('Rice Pilaf', 'Flavorful rice cooked with broth and spices'),
('Garlic Bread', 'Toasted bread with garlic butter'),
('Macaroni and Cheese', 'Creamy cheese sauce with macaroni'),
('Vegetable Soup', 'Hearty soup with mixed vegetables'),
('Apple Pie', 'Classic dessert with cinnamon-spiced apples'),
('Chocolate Cake', 'Rich and moist chocolate cake'),
('Guacamole', 'Fresh avocado dip with lime and cilantro'),
('Hummus', 'Creamy chickpea dip with tahini'),
('Fruit Salad', 'Fresh mixed fruits in a light syrup');

-- Insert Recipes
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Classic Spaghetti Carbonara', 'A creamy Italian pasta dish with eggs, cheese, pancetta, and black pepper', 3),
('Homemade Tomato Soup', 'A comforting soup made with fresh tomatoes, herbs, and cream', 4),
('Perfect Roasted Vegetables', 'A simple method for perfectly roasted seasonal vegetables', 6),
('Creamy Mashed Potatoes', 'Fluffy and creamy mashed potatoes with butter and milk', 7),
('Best Chocolate Chip Cookies', 'Soft and chewy cookies with chocolate chips', 8),
('Easy Chicken Stir Fry', 'Quick and flavorful chicken stir fry with vegetables', 10),
('Hearty Beef Stew', 'A comforting stew with tender beef and vegetables', 11),
('Classic Pancakes', 'Light and fluffy breakfast pancakes from scratch', 12),
('Simple Scrambled Eggs', 'Perfectly scrambled eggs every time', 14),
('Homemade Mac and Cheese', 'Creamy, cheesy macaroni and cheese', 19);

-- Insert Recipe Instructions
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(1, 1, 'Bring a large pot of salted water to boil.'),
(1, 2, 'Cook spaghetti according to package directions until al dente.'),
(1, 3, 'While pasta cooks, whisk together eggs, grated cheese, and black pepper in a bowl.'),
(1, 4, 'Cook bacon in a large skillet until crispy. Remove and chop.'),
(1, 5, 'Reserve some pasta water, then drain pasta.'),
(1, 6, 'Working quickly, add hot pasta to the skillet, then remove from heat.'),
(1, 7, 'Add the egg mixture, tossing continuously until creamy.'),
(1, 8, 'Add chopped bacon and thin with pasta water if needed.'),
(1, 9, 'Serve immediately with extra cheese and black pepper.');

-- Carbonara ingredients
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(1, 24, 1, 0.75),
(1, 12, 13, 2),
(1, 29, 1, 0.5),
(1, 2, 3, 1),
(1, 17, 5, 0.25);

-- Tomato Soup ingredients
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(2, 18, 13, 6),
(2, 6, 13, 1),
(2, 5, 11, 2),
(2, 3, 2, 2),
(2, 14, 1, 0.5),
(2, 1, 3, 1),
(2, 2, 3, 0.5);

-- Insert Meals
INSERT OR IGNORE INTO Meal (meal_name, meal_description) VALUES
('Weeknight Pasta Dinner', 'A simple and satisfying pasta dinner for busy weeknights'),
('Sunday Roast', 'Traditional Sunday dinner with all the fixings'),
('Breakfast Classics', 'A hearty breakfast with all the favorites'),
('Light Lunch', 'A balanced lunch that will not weigh you down'),
('Comfort Food Dinner', 'Classic comfort foods for a cozy evening');

-- Weeknight Pasta Dinner
INSERT OR IGNORE INTO MealFoodItem (mf_meal_id, mf_fooditem_id) VALUES
(1, 3),
(1, 18),
(1, 5);

-- Sunday Roast
INSERT OR IGNORE INTO MealFoodItem (mf_meal_id, mf_fooditem_id) VALUES
(2, 1),
(2, 7),
(2, 6),
(2, 21);

-- Breakfast Classics
INSERT OR IGNORE INTO MealFoodItem (mf_meal_id, mf_fooditem_id) VALUES
(3, 12),
(3, 14),
(3, 17),
(3, 25);

-- Light Lunch
INSERT OR IGNORE INTO MealFoodItem (mf_meal_id, mf_fooditem_id) VALUES
(4, 5),
(4, 16),
(4, 4);

-- Comfort Food Dinner
INSERT OR IGNORE INTO MealFoodItem (mf_meal_id, mf_fooditem_id) VALUES
(5, 19),
(5, 15),
(5, 20),
(5, 22);

-- Create categories
INSERT OR IGNORE INTO Category (category_name, category_description) VALUES
('Breakfast', 'Morning meals'),
('Lunch', 'Midday meals'),
('Dinner', 'Evening meals'),
('Dessert', 'Sweet treats'),
('Appetizer', 'Starters and snacks'),
('Italian', 'Italian cuisine'),
('American', 'American cuisine'),
('Vegetarian', 'Meatless dishes'),
('Quick & Easy', 'Fast recipes under 30 minutes'),
('Comfort Food', 'Hearty, satisfying dishes');

-- Link recipes to categories
INSERT OR IGNORE INTO RecipeCategory (recipe_id, category_id) VALUES
(1, 6),
(1, 3),
(2, 10),
(3, 8),
(8, 1),
(9, 1),
(9, 9);

-- Link ingredients to categories
INSERT OR IGNORE INTO IngredientCategory (ingredient_id, category_id) VALUES
(15, 3),
(16, 3),
(12, 1),
(25, 1);

-- Link meals to categories
INSERT OR IGNORE INTO MealCategory (meal_id, category_id) VALUES
(1, 3),
(2, 3),
(3, 1),
(4, 2),
(5, 10),
(4, 2), -- Light Lunch - Lunch
(5, 10), -- Comfort Food Dinner - Comfort Food
(5, 10); -- Comfort Food Dinner - Comfort Food */

-- Add instructions for all recipes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(3, 1, 'Preheat oven to 425°F (220°C).'),
(3, 2, 'Chop vegetables into even pieces.'),
(3, 3, 'Toss vegetables with olive oil, salt, and pepper.'),
(3, 4, 'Spread on a baking sheet and roast for 25-30 minutes, stirring halfway.'),
(3, 5, 'Serve hot.'),

(4, 1, 'Peel and cut potatoes into chunks.'),
(4, 2, 'Boil potatoes in salted water until tender.'),
(4, 3, 'Drain and mash potatoes.'),
(4, 4, 'Add butter and milk, then mix until creamy.'),
(4, 5, 'Season with salt and pepper.'),

(5, 1, 'Preheat oven to 350°F (175°C).'),
(5, 2, 'Cream together butter and sugars.'),
(5, 3, 'Add eggs and vanilla, mix well.'),
(5, 4, 'Stir in flour, baking soda, and salt.'),
(5, 5, 'Fold in chocolate chips.'),
(5, 6, 'Drop spoonfuls onto baking sheet and bake for 10-12 minutes.'),

(6, 1, 'Slice chicken breast and vegetables.'),
(6, 2, 'Heat oil in a wok or skillet.'),
(6, 3, 'Cook chicken until browned.'),
(6, 4, 'Add vegetables and stir fry until tender.'),
(6, 5, 'Add soy sauce and cook for 2 more minutes.'),

(7, 1, 'Cut beef into cubes.'),
(7, 2, 'Brown beef in a large pot.'),
(7, 3, 'Add chopped vegetables and cook for 5 minutes.'),
(7, 4, 'Add broth and seasonings, bring to a boil.'),
(7, 5, 'Simmer for 2 hours until beef is tender.'),

(8, 1, 'Mix flour, sugar, baking powder, and salt in a bowl.'),
(8, 2, 'Whisk milk, eggs, and melted butter together.'),
(8, 3, 'Combine wet and dry ingredients.'),
(8, 4, 'Pour batter onto hot griddle and cook until bubbles form.'),
(8, 5, 'Flip and cook until golden brown.'),

(9, 1, 'Crack eggs into a bowl and whisk.'),
(9, 2, 'Heat butter in a skillet over medium heat.'),
(9, 3, 'Pour eggs into skillet and stir gently.'),
(9, 4, 'Cook until just set, then serve.'),

(10, 1, 'Boil macaroni until al dente.'),
(10, 2, 'Make cheese sauce by melting butter, adding flour, then milk and cheese.'),
(10, 3, 'Combine macaroni and cheese sauce.'),
(10, 4, 'Pour into baking dish, top with more cheese, and bake until bubbly.');

-- Add ingredients for all recipes
-- Roasted Vegetables
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(3, 18, 13, 2), -- Tomato
(3, 19, 13, 1), -- Bell Pepper
(3, 20, 13, 1), -- Carrot
(3, 21, 13, 1), -- Celery
(3, 3, 2, 2),   -- Olive Oil
(3, 1, 3, 1),   -- Salt
(3, 2, 3, 0.5); -- Black Pepper

-- Mashed Potatoes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(4, 22, 13, 4), -- Potato
(4, 4, 2, 2),   -- Butter
(4, 13, 12, 0.5), -- Milk
(4, 1, 3, 1),   -- Salt
(4, 2, 3, 0.5); -- Black Pepper

-- Chocolate Chip Cookies
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(5, 7, 2, 2.25), -- Flour
(5, 8, 2, 1),    -- Sugar
(5, 9, 2, 1),    -- Brown Sugar
(5, 4, 2, 1),    -- Butter
(5, 12, 13, 2),  -- Eggs
(5, 41, 2, 2),   -- Vanilla Extract
(5, 1, 3, 0.5),  -- Salt
(5, 10, 2, 1),   -- Baking Powder
(5, 11, 2, 0.5); -- Baking Soda

-- Chicken Stir Fry
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(6, 15, 13, 2), -- Chicken Breast
(6, 19, 13, 1), -- Bell Pepper
(6, 20, 13, 1), -- Carrot
(6, 21, 13, 1), -- Celery
(6, 3, 2, 2),   -- Olive Oil
(6, 42, 2, 2),  -- Soy Sauce
(6, 1, 3, 1);   -- Salt

-- Beef Stew
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(7, 16, 13, 2), -- Ground Beef
(7, 20, 13, 2), -- Carrot
(7, 21, 13, 2), -- Celery
(7, 22, 13, 2), -- Potato
(7, 3, 2, 2),   -- Olive Oil
(7, 1, 3, 1),   -- Salt
(7, 2, 3, 0.5); -- Black Pepper

-- Pancakes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(8, 7, 2, 2),   -- Flour
(8, 8, 2, 1),   -- Sugar
(8, 12, 13, 2), -- Eggs
(8, 13, 12, 1.5), -- Milk
(8, 4, 2, 0.25), -- Butter
(8, 10, 2, 1),  -- Baking Powder
(8, 1, 3, 0.5); -- Salt

-- Scrambled Eggs
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(9, 12, 13, 3), -- Eggs
(9, 4, 2, 1),   -- Butter
(9, 1, 3, 0.25),-- Salt
(9, 2, 3, 0.25);-- Black Pepper

-- Mac and Cheese
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(10, 23, 13, 2), -- Pasta
(10, 25, 2, 2),  -- Cheese
(10, 13, 12, 1), -- Milk
(10, 4, 2, 2),   -- Butter
(10, 1, 3, 0.5), -- Salt
(10, 2, 3, 0.25);-- Black Pepper

-- Add more categories for variety
INSERT OR IGNORE INTO RecipeCategory (recipe_id, category_id) VALUES
(3, 8), -- Roasted Vegetables - Vegetarian
(4, 10), -- Mashed Potatoes - Comfort Food
(5, 4), -- Chocolate Chip Cookies - Dessert
(6, 9), -- Chicken Stir Fry - Quick & Easy
(7, 10), -- Beef Stew - Comfort Food
(8, 1), -- Pancakes - Breakfast
(9, 1), -- Scrambled Eggs - Breakfast
(10, 10); -- Mac and Cheese - Comfort Food

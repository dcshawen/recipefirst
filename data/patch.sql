-- /* /* -- Test data insertion script

-- Insert basic unit types('Mayonnaise', 'Real mayonnaise', 'Creamy base for dressings and sandwiches'),
INSERT OR IGNORE INTO Ingredient (ingredient_name, ingredient_description, ingredient_notes) VALUES
('Avocado', 'Ripe avocados', 'Yield to gentle pressure when ripe'),
('Chickpeas', 'Dried or canned chickpeas', 'Also called garbanzo beans'),
('Tahini', 'Sesame seed paste', 'Essential for authentic hummus'),
('Apples', 'Granny Smith or Honeycrisp apples', 'Tart varieties best for baking'),
('Blueberries', 'Fresh or frozen blueberries', 'Do not thaw if using frozen'),
('Cocoa Powder', 'Unsweetened cocoa powder', 'Dutch-process preferred for baking'),
('Chocolate Chips', 'Semi-sweet chocolate chips', 'Can substitute with chopped chocolate'),
('Lettuce', 'Romaine or mixed greens', 'Wash and dry thoroughly'),
('Croutons', 'Store-bought or homemade croutons', 'Add just before serving'),
('Caesar Dressing', 'Creamy Caesar dressing', 'Can make from scratch'),
('Vegetable Broth', 'Low-sodium vegetable broth', 'Foundation for soups'),
('Chicken Stock', 'Rich chicken stock', 'Homemade preferred but store-bought works'),
('Bananas', 'Ripe bananas', 'Perfect for baking when slightly overripe'),
('Buttermilk', 'Cultured buttermilk', 'Makes pancakes extra fluffy'),
('Whole Wheat Flour', 'Stone-ground whole wheat flour', 'More nutritious than all-purpose'),
('Pie Crust', 'Store-bought or homemade pie crust', 'Thaw if frozen before using'),
('Cake Flour', 'Fine cake flour', 'Creates lighter texture in cakes');

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

-- Insert ingredients with descriptions
INSERT OR IGNORE INTO Ingredient (ingredient_name, ingredient_description, ingredient_notes) VALUES
('Salt', 'Fine table salt for seasoning', 'Essential for enhancing flavors'),
('Black Pepper', 'Freshly ground black pepper', 'Best when freshly cracked'),
('Olive Oil', 'Extra virgin olive oil', 'Use for cooking and dressings'),
('Butter', 'Unsalted butter', 'Bring to room temperature for baking'),
('Garlic', 'Fresh garlic cloves', 'Mince or crush for best flavor'),
('Onion', 'Yellow cooking onion', 'Store in cool, dry place'),
('Flour', 'All-purpose flour', 'Sift for lighter texture in baking'),
('Sugar', 'Granulated white sugar', 'Standard sweetener for baking'),
('Brown Sugar', 'Light or dark brown sugar', 'Packed when measuring'),
('Baking Powder', 'Double-acting baking powder', 'Check expiration date'),
('Baking Soda', 'Sodium bicarbonate', 'Creates lift in baked goods'),
('Eggs', 'Large eggs', 'Room temperature eggs mix better'),
('Milk', 'Whole milk', 'Can substitute with 2% if needed'),
('Heavy Cream', '35% fat heavy whipping cream', 'Essential for rich sauces'),
('Chicken Breast', 'Boneless, skinless chicken breast', 'Pound to even thickness'),
('Ground Beef', 'Lean ground beef, 80/20 blend', 'Use within 2 days of purchase'),
('Bacon', 'Thick-cut bacon strips', 'Cook until crispy for best texture'),
('Tomato', 'Fresh ripe tomatoes', 'Choose firm, red tomatoes'),
('Bell Pepper', 'Sweet bell peppers', 'Any color works well'),
('Carrot', 'Fresh carrots', 'Peel before using'),
('Celery', 'Fresh celery stalks', 'Crisp and green'),
('Potato', 'Russet or Yukon Gold potatoes', 'Great for mashing and roasting'),
('Rice', 'Long-grain white rice', 'Rinse until water runs clear'),
('Pasta', 'Dried pasta, various shapes', 'Cook al dente for best texture'),
('Bread', 'Sliced white or wheat bread', 'Day-old bread works for some recipes'),
('Cheese', 'General cheese for cooking', 'Grate fresh for best melting'),
('Cheddar Cheese', 'Sharp cheddar cheese', 'Ages well, great melting cheese'),
('Mozzarella Cheese', 'Whole milk mozzarella', 'Perfect for pizza and pasta'),
('Parmesan Cheese', 'Parmigiano-Reggiano', 'Aged hard cheese, grate fresh'),
('Lemon', 'Fresh lemons', 'Roll to get more juice'),
('Lime', 'Fresh limes', 'Great for Mexican and Asian dishes'),
('Cilantro', 'Fresh cilantro leaves', 'Also called coriander leaf'),
('Parsley', 'Fresh flat-leaf parsley', 'More flavor than curly parsley'),
('Basil', 'Fresh basil leaves', 'Essential for Italian cooking'),
('Rosemary', 'Fresh rosemary sprigs', 'Woody herb, use sparingly'),
('Thyme', 'Fresh thyme sprigs', 'Versatile herb for meat and vegetables'),
('Oregano', 'Dried oregano', 'Staple of Mediterranean cuisine'),
('Cinnamon', 'Ground cinnamon', 'Warm spice for sweet and savory'),
('Cumin', 'Ground cumin seeds', 'Earthy spice for Mexican and Indian food'),
('Paprika', 'Sweet or smoked paprika', 'Adds color and mild pepper flavor'),
('Cayenne Pepper', 'Ground cayenne pepper', 'Use sparingly, very hot'),
('Nutmeg', 'Ground nutmeg', 'Warm spice for desserts and cream sauces'),
('Vanilla Extract', 'Pure vanilla extract', 'Essential for baking'),
('Soy Sauce', 'Low-sodium soy sauce', 'Umami-rich condiment'),
('Honey', 'Pure honey', 'Natural sweetener'),
('Maple Syrup', 'Pure maple syrup', 'Grade A amber color'),
('Vinegar', 'White distilled vinegar', 'For cleaning and cooking'),
('Red Wine Vinegar', 'Aged red wine vinegar', 'Great for dressings'),
('Mustard', 'Dijon mustard', 'Sharp, tangy condiment'),
('Mayonnaise', 'Real mayonnaise', 'Creamy base for dressings and sandwiches'),
('Avocado', 'Ripe avocados', 'Yield to gentle pressure when ripe'),
('Chickpeas', 'Dried or canned chickpeas', 'Also called garbanzo beans'),
('Tahini', 'Sesame seed paste', 'Essential for authentic hummus'),
('Apples', 'Granny Smith or Honeycrisp apples', 'Tart varieties best for baking'),
('Blueberries', 'Fresh or frozen blueberries', 'Do not thaw if using frozen'),
('Cocoa Powder', 'Unsweetened cocoa powder', 'Dutch-process preferred for baking'),
('Chocolate Chips', 'Semi-sweet chocolate chips', 'Can substitute with chopped chocolate'),
('Lettuce', 'Romaine or mixed greens', 'Wash and dry thoroughly'),
('Croutons', 'Store-bought or homemade croutons', 'Add just before serving'),
('Caesar Dressing', 'Creamy Caesar dressing', 'Can make from scratch'),
('Vegetable Broth', 'Low-sodium vegetable broth', 'Foundation for soups'),
('Chicken Stock', 'Rich chicken stock', 'Homemade preferred but store-bought works');

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
(15, 3), -- Chicken Breast - Dinner
(16, 3), -- Ground Beef - Dinner
(12, 1), -- Eggs - Breakfast
(25, 1), -- Bread - Breakfast
(7, 4), -- Flour - Dessert (baking)
(8, 4), -- Sugar - Dessert
(9, 4), -- Brown Sugar - Dessert
(43, 4), -- Vanilla Extract - Dessert
(55, 4), -- Chocolate Chips - Dessert
(52, 4), -- Blueberries - Dessert
(53, 4), -- Apples - Dessert
(50, 8), -- Avocado - Vegetarian
(51, 8), -- Chickpeas - Vegetarian
(56, 8), -- Lettuce - Vegetarian
(18, 8), -- Tomato - Vegetarian
(19, 8), -- Bell Pepper - Vegetarian
(20, 8), -- Carrot - Vegetarian
(23, 3), -- Rice - Dinner
(24, 3); -- Pasta - Dinner

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
(10, 24, 5, 1), -- Pasta
(10, 27, 1, 2),  -- Cheddar Cheese
(10, 13, 1, 2), -- Milk
(10, 4, 2, 4),   -- Butter
(10, 7, 2, 0.25), -- Flour
(10, 1, 3, 0.5), -- Salt
(10, 2, 3, 0.25);-- Black Pepper

-- Add ingredients for new recipes (11-25)

-- Recipe 11: Simple Grilled Chicken Breast
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(11, 15, 5, 1.5), -- Chicken Breast
(11, 1, 3, 1), -- Salt
(11, 2, 3, 0.5), -- Black Pepper
(11, 36, 2, 1), -- Thyme
(11, 3, 2, 2); -- Olive Oil

-- Recipe 12: Classic Beef Burger
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(12, 16, 5, 1), -- Ground Beef
(12, 25, 13, 4), -- Bread (buns)
(12, 27, 12, 4), -- Cheddar Cheese slices
(12, 18, 13, 1), -- Tomato
(12, 1, 3, 1), -- Salt
(12, 2, 3, 0.5); -- Black Pepper

-- Recipe 13: Fresh Caesar Salad
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(13, 56, 13, 2), -- Lettuce (using lettuce ingredient)
(13, 29, 1, 0.5), -- Parmesan Cheese
(13, 30, 13, 1); -- Lemon

-- Recipe 14: Fluffy Blueberry Muffins
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(14, 7, 1, 2), -- Flour
(14, 8, 1, 0.75), -- Sugar
(14, 10, 2, 2), -- Baking Powder
(14, 1, 3, 0.5), -- Salt
(14, 13, 1, 1), -- Milk
(14, 12, 13, 2), -- Eggs
(14, 4, 2, 6), -- Butter (melted)
(14, 43, 3, 2), -- Vanilla Extract
(14, 52, 1, 1); -- Blueberries

-- Recipe 15: Classic French Toast
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(15, 25, 12, 8), -- Bread slices
(15, 12, 13, 4), -- Eggs
(15, 13, 1, 0.5), -- Milk
(15, 43, 3, 1), -- Vanilla Extract
(15, 38, 3, 0.5), -- Cinnamon
(15, 4, 2, 2), -- Butter
(15, 45, 2, 2); -- Maple Syrup

-- Recipe 16: Perfect Grilled Cheese
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(16, 25, 12, 4), -- Bread slices
(16, 27, 12, 4), -- Cheddar Cheese slices
(16, 4, 2, 2); -- Butter

-- Recipe 17: Fresh Garden Salad
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(17, 56, 13, 1), -- Lettuce
(17, 18, 13, 2), -- Tomato
(17, 20, 13, 1), -- Carrot
(17, 19, 13, 1), -- Bell Pepper
(17, 3, 2, 2), -- Olive Oil
(17, 46, 2, 1); -- Vinegar

-- Recipe 18: Savory Rice Pilaf
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(18, 23, 1, 1), -- Rice
(18, 6, 13, 1), -- Onion
(18, 3, 2, 2), -- Olive Oil
(18, 1, 3, 1), -- Salt
(18, 36, 3, 1); -- Thyme

-- Recipe 19: Homemade Garlic Bread
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(19, 25, 13, 1), -- Bread loaf
(19, 4, 2, 6), -- Butter
(19, 5, 11, 4), -- Garlic cloves
(19, 33, 2, 2); -- Parsley

-- Recipe 20: Hearty Vegetable Soup
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(20, 18, 13, 3), -- Tomato
(20, 20, 13, 2), -- Carrot
(20, 21, 13, 2), -- Celery
(20, 6, 13, 1), -- Onion
(20, 3, 2, 2), -- Olive Oil
(20, 1, 3, 1), -- Salt
(20, 2, 3, 0.5); -- Black Pepper

-- Add ingredients for multiple recipe variations

-- Recipe 26: Fluffy Buttermilk Pancakes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(26, 7, 1, 2), -- Flour
(26, 8, 2, 2), -- Sugar
(26, 10, 3, 1), -- Baking Powder
(26, 11, 3, 0.5), -- Baking Soda
(26, 1, 3, 1), -- Salt
(26, 13, 1, 1.75), -- Milk (substitute for buttermilk)
(26, 12, 13, 2), -- Eggs
(26, 4, 2, 4); -- Butter (melted)

-- Recipe 27: Whole Wheat Pancakes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(27, 7, 1, 2), -- Flour (whole wheat)
(27, 8, 2, 2), -- Sugar
(27, 10, 3, 2), -- Baking Powder
(27, 1, 3, 0.5), -- Salt
(27, 13, 1, 1.5), -- Milk
(27, 12, 13, 1), -- Eggs
(27, 3, 2, 2); -- Olive Oil

-- Recipe 28: Banana Pancakes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(28, 7, 1, 1.5), -- Flour
(28, 8, 2, 1), -- Sugar
(28, 10, 3, 2), -- Baking Powder
(28, 1, 3, 0.5), -- Salt
(28, 38, 3, 0.5), -- Cinnamon
(28, 12, 13, 2), -- Eggs
(28, 13, 1, 1), -- Milk
(28, 43, 3, 1), -- Vanilla Extract
(28, 61, 13, 2); -- Bananas

-- Recipe 21: Classic Apple Pie
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(21, 53, 13, 6), -- Apples
(21, 8, 1, 0.75), -- Sugar
(21, 38, 3, 2), -- Cinnamon
(21, 42, 3, 0.25), -- Nutmeg
(21, 7, 2, 2), -- Flour (for thickening)
(21, 4, 2, 2), -- Butter
(21, 64, 13, 2); -- Pie Crust

-- Recipe 22: Rich Chocolate Cake
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(22, 65, 1, 1.75), -- Cake Flour
(22, 8, 1, 2), -- Sugar
(22, 54, 1, 0.75), -- Cocoa Powder
(22, 11, 3, 2), -- Baking Soda
(22, 1, 3, 1), -- Salt
(22, 12, 13, 2), -- Eggs
(22, 13, 1, 1), -- Milk
(22, 3, 1, 0.5), -- Oil
(22, 43, 3, 2); -- Vanilla Extract

-- Recipe 23: Fresh Guacamole
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(23, 50, 13, 3), -- Avocado
(23, 31, 13, 2), -- Lime
(23, 5, 11, 2), -- Garlic
(23, 6, 2, 0.25), -- Onion
(23, 32, 2, 2), -- Cilantro
(23, 1, 3, 1); -- Salt

-- Recipe 24: Creamy Hummus
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(24, 51, 1, 1.5), -- Chickpeas
(24, 52, 2, 0.25), -- Tahini
(24, 30, 13, 1), -- Lemon
(24, 5, 11, 2), -- Garlic
(24, 3, 2, 2), -- Olive Oil
(24, 39, 3, 0.5), -- Cumin
(24, 1, 3, 1); -- Salt

-- Recipe 25: Rainbow Fruit Salad
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(25, 53, 13, 2), -- Apples
(25, 61, 13, 2), -- Bananas
(25, 52, 1, 1), -- Blueberries
(25, 44, 2, 3), -- Honey
(25, 31, 13, 1); -- Lime

-- Add ingredients for additional multiple recipe variations

-- Recipe 29: French-Style Scrambled Eggs
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(29, 12, 13, 6), -- Eggs
(29, 4, 2, 3), -- Butter
(29, 14, 2, 2), -- Heavy Cream
(29, 1, 3, 0.5); -- Salt

-- Recipe 30: Herb Scrambled Eggs
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(30, 12, 13, 6), -- Eggs
(30, 4, 2, 2), -- Butter
(30, 14, 2, 2), -- Heavy Cream
(30, 33, 2, 1), -- Parsley
(30, 34, 2, 1), -- Basil
(30, 1, 3, 0.5); -- Salt

-- Recipe 31: Crispy Chocolate Chip Cookies
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(31, 7, 1, 2.25), -- Flour
(31, 8, 1, 0.75), -- Sugar
(31, 9, 1, 0.75), -- Brown Sugar
(31, 4, 2, 1), -- Butter
(31, 12, 13, 1), -- Eggs
(31, 43, 3, 1), -- Vanilla Extract
(31, 11, 3, 1), -- Baking Soda
(31, 1, 3, 1), -- Salt
(31, 55, 1, 2); -- Chocolate Chips

-- Recipe 32: Chewy Chocolate Chip Cookies
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(32, 7, 1, 2.25), -- Flour
(32, 8, 1, 0.5), -- Sugar
(32, 9, 1, 1), -- Brown Sugar (more for chewiness)
(32, 4, 2, 1), -- Butter (melted)
(32, 12, 13, 1), -- Eggs
(32, 43, 3, 1), -- Vanilla Extract
(32, 11, 3, 1), -- Baking Soda
(32, 1, 3, 1), -- Salt
(32, 55, 1, 2); -- Chocolate Chips

-- Recipe 33: Authentic Roman Carbonara
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(33, 24, 5, 1), -- Pasta
(33, 17, 4, 0.25), -- Bacon (substitute for guanciale)
(33, 12, 13, 4), -- Eggs (yolks)
(33, 29, 1, 1), -- Parmesan Cheese
(33, 2, 3, 1); -- Black Pepper

-- Recipe 34: Quick Weeknight Carbonara
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(34, 24, 5, 1), -- Pasta
(34, 17, 4, 0.25), -- Bacon
(34, 12, 13, 2), -- Eggs (whole)
(34, 14, 2, 0.25), -- Heavy Cream
(34, 29, 1, 0.75), -- Parmesan Cheese
(34, 2, 3, 1); -- Black Pepper

-- Recipe 35: Garlic Mashed Potatoes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(35, 22, 5, 3), -- Potato
(35, 5, 13, 1), -- Garlic (whole head for roasting)
(35, 4, 2, 4), -- Butter
(35, 13, 1, 0.5), -- Milk
(35, 1, 3, 1), -- Salt
(35, 2, 3, 0.5); -- Black Pepper

-- Recipe 36: Loaded Mashed Potatoes
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(36, 22, 5, 3), -- Potato
(36, 4, 2, 4), -- Butter
(36, 14, 1, 0.5), -- Heavy Cream
(36, 27, 1, 1), -- Cheddar Cheese
(36, 17, 12, 6), -- Bacon (cooked and crumbled)
(36, 32, 2, 2), -- Chives (substitute with parsley)
(36, 1, 3, 1), -- Salt
(36, 2, 3, 0.5); -- Black Pepper

-- Add instructions for all new recipes (starting from recipe 11)

-- Recipe 11: Simple Grilled Chicken Breast
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(11, 1, 'Preheat grill to medium-high heat.'),
(11, 2, 'Season chicken breasts with salt, pepper, and herbs.'),
(11, 3, 'Oil the grill grates to prevent sticking.'),
(11, 4, 'Grill chicken for 6-7 minutes per side until internal temp reaches 165°F.'),
(11, 5, 'Let rest for 5 minutes before serving.');

-- Recipe 12: Classic Beef Burger
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(12, 1, 'Form ground beef into 4 patties, season with salt and pepper.'),
(12, 2, 'Heat grill or skillet to medium-high heat.'),
(12, 3, 'Cook burgers 4-5 minutes per side for medium doneness.'),
(12, 4, 'Add cheese in the last minute if desired.'),
(12, 5, 'Serve on toasted buns with desired toppings.');

-- Recipe 13: Fresh Caesar Salad
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(13, 1, 'Wash and chop romaine lettuce into bite-sized pieces.'),
(13, 2, 'Make dressing by whisking together mayo, lemon juice, garlic, and anchovies.'),
(13, 3, 'Toss lettuce with dressing until well coated.'),
(13, 4, 'Top with parmesan cheese and croutons.'),
(13, 5, 'Serve immediately.');

-- Recipe 14: Fluffy Blueberry Muffins
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(14, 1, 'Preheat oven to 375°F and line muffin tin with paper liners.'),
(14, 2, 'Mix flour, sugar, baking powder, and salt in a large bowl.'),
(14, 3, 'Whisk together milk, eggs, melted butter, and vanilla.'),
(14, 4, 'Fold wet ingredients into dry ingredients until just combined.'),
(14, 5, 'Gently fold in blueberries.'),
(14, 6, 'Fill muffin cups 2/3 full and bake for 20-25 minutes until golden.');

-- Recipe 15: Classic French Toast
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(15, 1, 'Whisk together eggs, milk, vanilla, and cinnamon.'),
(15, 2, 'Heat butter in a large skillet over medium heat.'),
(15, 3, 'Dip bread slices in egg mixture, coating both sides.'),
(15, 4, 'Cook 2-3 minutes per side until golden brown.'),
(15, 5, 'Serve hot with maple syrup and butter.');

-- Recipe 16: Perfect Grilled Cheese
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(16, 1, 'Butter one side of each bread slice.'),
(16, 2, 'Place cheese between bread slices, butter side out.'),
(16, 3, 'Heat skillet over medium-low heat.'),
(16, 4, 'Cook sandwich 3-4 minutes per side until golden and cheese melts.'),
(16, 5, 'Cut diagonally and serve hot.');

-- Recipe 17: Fresh Garden Salad
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(17, 1, 'Wash and dry mixed lettuce thoroughly.'),
(17, 2, 'Chop tomatoes, cucumbers, and carrots.'),
(17, 3, 'Combine vegetables in a large bowl.'),
(17, 4, 'Toss with your favorite dressing just before serving.'),
(17, 5, 'Garnish with croutons if desired.');

-- Recipe 18: Savory Rice Pilaf
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(18, 1, 'Heat oil in a saucepan and sauté onions until translucent.'),
(18, 2, 'Add rice and stir for 2 minutes until lightly toasted.'),
(18, 3, 'Pour in chicken stock and bring to a boil.'),
(18, 4, 'Reduce heat, cover, and simmer 18 minutes.'),
(18, 5, 'Let stand 5 minutes, then fluff with a fork and season.');

-- Recipe 19: Homemade Garlic Bread
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(19, 1, 'Preheat oven to 400°F.'),
(19, 2, 'Mix softened butter with minced garlic and parsley.'),
(19, 3, 'Slice bread and spread garlic butter on each piece.'),
(19, 4, 'Wrap in foil and bake for 15 minutes.'),
(19, 5, 'Unwrap and bake 5 more minutes for crispy top.');

-- Recipe 20: Hearty Vegetable Soup
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(20, 1, 'Chop all vegetables into uniform pieces.'),
(20, 2, 'Heat oil in a large pot and sauté onions and garlic.'),
(20, 3, 'Add remaining vegetables and cook 5 minutes.'),
(20, 4, 'Pour in vegetable broth and bring to a boil.'),
(20, 5, 'Simmer 20-25 minutes until vegetables are tender.'),
(20, 6, 'Season with salt, pepper, and herbs.');

-- Instructions for Multiple Pancake Recipes
-- Recipe 26: Fluffy Buttermilk Pancakes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(26, 1, 'Mix flour, sugar, baking powder, baking soda, and salt.'),
(26, 2, 'Whisk buttermilk, eggs, and melted butter separately.'),
(26, 3, 'Combine wet and dry ingredients until just mixed.'),
(26, 4, 'Let batter rest 5 minutes for extra fluffiness.'),
(26, 5, 'Cook on hot griddle until bubbles form and edges look set.');

-- Recipe 27: Whole Wheat Pancakes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(27, 1, 'Combine whole wheat flour, baking powder, salt, and a touch of sugar.'),
(27, 2, 'Whisk milk, eggs, and a little oil together.'),
(27, 3, 'Mix wet and dry ingredients gently to avoid tough pancakes.'),
(27, 4, 'Cook on medium heat griddle until golden brown.'),
(27, 5, 'Serve with fresh fruit and honey.');

-- Recipe 28: Banana Pancakes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(28, 1, 'Mash ripe bananas until smooth.'),
(28, 2, 'Mix flour, baking powder, salt, and cinnamon.'),
(28, 3, 'Combine mashed bananas, eggs, milk, and vanilla.'),
(28, 4, 'Fold banana mixture into dry ingredients.'),
(28, 5, 'Cook on griddle until golden, about 3 minutes per side.');

-- Recipe 21: Classic Apple Pie
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(21, 1, 'Preheat oven to 425°F and prepare pie crust in 9-inch pie pan.'),
(21, 2, 'Peel, core, and slice apples into thin wedges.'),
(21, 3, 'Mix apples with sugar, cinnamon, nutmeg, and a little flour.'),
(21, 4, 'Fill pie crust with apple mixture and dot with butter.'),
(21, 5, 'Cover with top crust, seal edges, and cut steam vents.'),
(21, 6, 'Bake 45-50 minutes until crust is golden and filling bubbles.');

-- Recipe 22: Rich Chocolate Cake
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(22, 1, 'Preheat oven to 350°F and grease two 9-inch cake pans.'),
(22, 2, 'Mix flour, sugar, cocoa powder, baking soda, and salt.'),
(22, 3, 'Whisk together eggs, milk, oil, and vanilla.'),
(22, 4, 'Combine wet and dry ingredients until smooth.'),
(22, 5, 'Divide batter between pans and bake 30-35 minutes.'),
(22, 6, 'Cool completely before frosting.');

-- Recipe 23: Fresh Guacamole
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(23, 1, 'Cut avocados in half, remove pits, and scoop into bowl.'),
(23, 2, 'Mash avocados with a fork, leaving some chunks.'),
(23, 3, 'Add lime juice, minced garlic, and diced onion.'),
(23, 4, 'Stir in chopped cilantro and season with salt.'),
(23, 5, 'Taste and adjust lime and salt as needed.'),
(23, 6, 'Serve immediately with tortilla chips.');

-- Recipe 24: Creamy Hummus
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(24, 1, 'Drain and rinse chickpeas, reserving liquid.'),
(24, 2, 'Combine chickpeas, tahini, lemon juice, and garlic in food processor.'),
(24, 3, 'Process until smooth, adding reserved liquid as needed.'),
(24, 4, 'Season with salt and cumin to taste.'),
(24, 5, 'Drizzle with olive oil before serving.'),
(24, 6, 'Serve with pita chips or fresh vegetables.');

-- Recipe 25: Rainbow Fruit Salad
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(25, 1, 'Wash all fruits thoroughly and pat dry.'),
(25, 2, 'Cut larger fruits into bite-sized pieces.'),
(25, 3, 'Combine all fruits in a large serving bowl.'),
(25, 4, 'Drizzle with honey and lime juice.'),
(25, 5, 'Toss gently to coat all fruit.'),
(25, 6, 'Chill for 30 minutes before serving.');

-- Instructions for additional multiple recipes

-- Recipe 29: French-Style Scrambled Eggs
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(29, 1, 'Crack eggs into a cold saucepan and whisk thoroughly.'),
(29, 2, 'Add butter and place over very low heat.'),
(29, 3, 'Stir constantly with a wooden spoon for 10-15 minutes.'),
(29, 4, 'Remove from heat when eggs are just set but still creamy.'),
(29, 5, 'Season with salt and serve immediately.');

-- Recipe 30: Herb Scrambled Eggs
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(30, 1, 'Whisk eggs with chopped fresh herbs and cream.'),
(30, 2, 'Heat butter in a non-stick pan over medium-low heat.'),
(30, 3, 'Pour in egg mixture and let sit for 30 seconds.'),
(30, 4, 'Gently stir and fold until eggs are just set.'),
(30, 5, 'Remove from heat and serve garnished with more herbs.');

-- Recipe 31: Crispy Chocolate Chip Cookies
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(31, 1, 'Preheat oven to 375°F for crispier cookies.'),
(31, 2, 'Cream butter and sugars until very light and fluffy.'),
(31, 3, 'Beat in eggs and vanilla extract.'),
(31, 4, 'Mix in flour, baking soda, and salt.'),
(31, 5, 'Stir in chocolate chips and drop on ungreased sheets.'),
(31, 6, 'Bake 9-11 minutes until golden brown.');

-- Recipe 32: Chewy Chocolate Chip Cookies
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(32, 1, 'Preheat oven to 325°F for chewier texture.'),
(32, 2, 'Use melted butter instead of softened for chewiness.'),
(32, 3, 'Mix in brown sugar for extra moisture.'),
(32, 4, 'Add flour mixture gradually to prevent overmixing.'),
(32, 5, 'Chill dough for 30 minutes before baking.'),
(32, 6, 'Bake 12-14 minutes until edges are set.');

-- Recipe 33: Authentic Roman Carbonara
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(33, 1, 'Cook guanciale (or pancetta) until crispy and golden.'),
(33, 2, 'Whisk egg yolks with grated Pecorino Romano cheese.'),
(33, 3, 'Cook pasta in well-salted water until al dente.'),
(33, 4, 'Reserve pasta water, then drain pasta.'),
(33, 5, 'Toss hot pasta with guanciale and its rendered fat.'),
(33, 6, 'Remove from heat and quickly stir in egg mixture.'),
(33, 7, 'Add pasta water gradually until creamy, not scrambled.');

-- Recipe 34: Quick Weeknight Carbonara
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(34, 1, 'Cook bacon in a large skillet until crispy.'),
(34, 2, 'Whisk together eggs, cream, and parmesan cheese.'),
(34, 3, 'Cook pasta according to package directions.'),
(34, 4, 'Drain pasta and immediately add to skillet with bacon.'),
(34, 5, 'Pour egg mixture over hot pasta and toss quickly.'),
(34, 6, 'Serve immediately with extra cheese and black pepper.');

-- Recipe 35: Garlic Mashed Potatoes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(35, 1, 'Roast whole garlic head in oven at 400°F for 30 minutes until soft.'),
(35, 2, 'Peel and cube potatoes, then boil in salted water until tender.'),
(35, 3, 'Squeeze roasted garlic cloves from skins and mash.'),
(35, 4, 'Drain potatoes and mash with butter and roasted garlic.'),
(35, 5, 'Gradually add warm milk until desired consistency.'),
(35, 6, 'Season with salt and pepper, serve hot.');

-- Recipe 36: Loaded Mashed Potatoes
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(36, 1, 'Cook bacon until crispy, then crumble and set aside.'),
(36, 2, 'Boil peeled, cubed potatoes in salted water until very tender.'),
(36, 3, 'Drain potatoes thoroughly and mash until smooth.'),
(36, 4, 'Beat in butter and heavy cream until fluffy.'),
(36, 5, 'Fold in cheese, most of the bacon, and chives.'),
(36, 6, 'Top with remaining bacon and cheese, serve immediately.');

-- Add more categories for variety
INSERT OR IGNORE INTO RecipeCategory (recipe_id, category_id) VALUES
(3, 8), -- Roasted Vegetables - Vegetarian
(4, 10), -- Mashed Potatoes - Comfort Food
(5, 4), -- Chocolate Chip Cookies - Dessert
(6, 9), -- Chicken Stir Fry - Quick & Easy
(7, 10), -- Beef Stew - Comfort Food
(8, 1), -- Pancakes - Breakfast
(9, 1), -- Scrambled Eggs - Breakfast
(10, 10), -- Mac and Cheese - Comfort Food
(11, 3), -- Grilled Chicken - Dinner
(12, 2), -- Beef Burger - Lunch
(13, 2), -- Caesar Salad - Lunch
(14, 1), -- Blueberry Muffins - Breakfast
(15, 1), -- French Toast - Breakfast
(16, 2), -- Grilled Cheese - Lunch
(17, 8), -- Garden Salad - Vegetarian
(18, 3), -- Rice Pilaf - Dinner
(19, 5), -- Garlic Bread - Appetizer
(20, 8), -- Vegetable Soup - Vegetarian
(26, 1), -- Buttermilk Pancakes - Breakfast
(27, 1), -- Whole Wheat Pancakes - Breakfast
(28, 1), -- Banana Pancakes - Breakfast
(21, 4), -- Apple Pie - Dessert
(22, 4), -- Chocolate Cake - Dessert
(23, 5), -- Guacamole - Appetizer
(23, 8), -- Guacamole - Vegetarian
(24, 5), -- Hummus - Appetizer
(24, 8), -- Hummus - Vegetarian
(25, 4), -- Fruit Salad - Dessert
(25, 8), -- Fruit Salad - Vegetarian
(29, 1), -- French-Style Scrambled Eggs - Breakfast
(30, 1), -- Herb Scrambled Eggs - Breakfast
(31, 4), -- Crispy Chocolate Chip Cookies - Dessert
(32, 4), -- Chewy Chocolate Chip Cookies - Dessert
(33, 6), -- Authentic Roman Carbonara - Italian
(33, 3), -- Authentic Roman Carbonara - Dinner
(34, 6), -- Quick Weeknight Carbonara - Italian
(34, 9), -- Quick Weeknight Carbonara - Quick & Easy
(35, 10), -- Garlic Mashed Potatoes - Comfort Food
(35, 3), -- Garlic Mashed Potatoes - Dinner
(36, 10), -- Loaded Mashed Potatoes - Comfort Food
(36, 3); -- Loaded Mashed Potatoes - Dinner

-- Insert Recipes for FoodItems that do not have a recipe yet
-- FoodItem IDs: 1 to 25
-- Existing recipes cover: 3, 4, 6, 7, 8, 10, 11, 12, 14, 19

-- Grilled Chicken Breast
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Simple Grilled Chicken Breast', 'Grilled chicken breast with basic seasoning', 1);

-- Classic Beef Burger
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Classic Beef Burger', 'Juicy beef patty with classic toppings', 2);

-- Caesar Salad
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Caesar Salad', 'Romaine lettuce with Caesar dressing and croutons', 5);

-- Roasted Vegetables (already covered by recipe 3)

-- Mashed Potatoes (already covered by recipe 4)

-- Chocolate Chip Cookies (already covered by recipe 5)

-- Blueberry Muffins
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Blueberry Muffins', 'Fluffy muffins with fresh blueberries', 9);

-- Chicken Stir Fry (already covered by recipe 6)

-- Beef Stew (already covered by recipe 7)

-- Pancakes (already covered by recipe 8)

-- French Toast
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('French Toast', 'Classic breakfast french toast', 13);

-- Scrambled Eggs (already covered by recipe 9)

-- Grilled Cheese Sandwich
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Grilled Cheese Sandwich', 'Classic comfort food sandwich', 15);

-- Garden Salad
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Garden Salad', 'Fresh mixed greens with vegetables', 16);

-- Rice Pilaf
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Rice Pilaf', 'Flavorful rice cooked with broth and spices', 17);

-- Garlic Bread
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Garlic Bread', 'Toasted bread with garlic butter', 18);

-- Macaroni and Cheese (already covered by recipe 10)

-- Vegetable Soup
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Vegetable Soup', 'Hearty soup with mixed vegetables', 20);

-- Apple Pie
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Apple Pie', 'Classic dessert with cinnamon-spiced apples', 21);

-- Chocolate Cake
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Chocolate Cake', 'Rich and moist chocolate cake', 22);

-- Guacamole
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Guacamole', 'Fresh avocado dip with lime and cilantro', 23);

-- Hummus
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Hummus', 'Creamy chickpea dip with tahini', 24);

-- Fruit Salad
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Fruit Salad', 'Fresh mixed fruits in a light syrup', 25);

-- Add complete recipes for missing FoodItems with proper recipe IDs starting from 11
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Simple Grilled Chicken Breast', 'Perfectly seasoned grilled chicken breast', 1),
('Classic Beef Burger', 'Juicy beef patty with all the fixings', 2),
('Fresh Caesar Salad', 'Crisp romaine with creamy Caesar dressing', 5),
('Fluffy Blueberry Muffins', 'Bakery-style muffins packed with blueberries', 9),
('Classic French Toast', 'Custardy French toast with cinnamon', 13),
('Perfect Grilled Cheese', 'Golden, crispy sandwich with melted cheese', 15),
('Fresh Garden Salad', 'Mixed greens with seasonal vegetables', 16),
('Savory Rice Pilaf', 'Aromatic rice with herbs and spices', 17),
('Homemade Garlic Bread', 'Crispy bread with garlic butter', 18),
('Hearty Vegetable Soup', 'Comforting soup with garden vegetables', 20),
('Classic Apple Pie', 'Traditional pie with cinnamon-spiced apples', 21),
('Rich Chocolate Cake', 'Decadent chocolate layer cake', 22),
('Fresh Guacamole', 'Creamy avocado dip with lime and cilantro', 23),
('Creamy Hummus', 'Smooth chickpea dip with tahini', 24),
('Rainbow Fruit Salad', 'Fresh seasonal fruits with light dressing', 25);

-- Add MULTIPLE recipes for the SAME FoodItems to demonstrate one-to-many relationships
-- Multiple Pancake Recipes (FoodItem #12) - Recipes 26, 27, 28
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Fluffy Buttermilk Pancakes', 'Extra fluffy pancakes made with buttermilk', 12),
('Whole Wheat Pancakes', 'Healthier pancakes with whole wheat flour', 12),
('Banana Pancakes', 'Sweet pancakes with mashed bananas', 12);

-- Multiple Scrambled Eggs Recipes (FoodItem #14) - Recipes 29, 30
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('French-Style Scrambled Eggs', 'Creamy, slow-cooked scrambled eggs', 14),
('Herb Scrambled Eggs', 'Eggs scrambled with fresh herbs', 14);

-- Multiple Chocolate Chip Cookie Recipes (FoodItem #8) - Recipes 31, 32
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Crispy Chocolate Chip Cookies', 'Thin and crispy chocolate chip cookies', 8),
('Chewy Chocolate Chip Cookies', 'Soft and chewy chocolate chip cookies', 8);

-- Multiple Spaghetti Carbonara Recipes (FoodItem #3) - Recipes 33, 34
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Authentic Roman Carbonara', 'Traditional carbonara with guanciale', 3),
('Quick Weeknight Carbonara', 'Simplified carbonara for busy nights', 3);

-- Multiple Mashed Potato Recipes (FoodItem #7) - Recipes 35, 36
INSERT OR IGNORE INTO Recipe (recipe_name, recipe_description, recipe_fooditem_id) VALUES
('Garlic Mashed Potatoes', 'Creamy mashed potatoes with roasted garlic', 7),
('Loaded Mashed Potatoes', 'Mashed potatoes with cheese, bacon, and chives', 7);

-- Add missing ingredients and instructions for the duplicate recipe entries (recipes from the second batch)

-- Ingredients for the additional recipes that were missing them
-- Recipe 37: Simple Grilled Chicken Breast (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(37, 15, 5, 1.5), -- Chicken Breast
(37, 3, 2, 2), -- Olive Oil
(37, 1, 3, 1), -- Salt
(37, 2, 3, 0.5), -- Black Pepper
(37, 5, 11, 2); -- Garlic

-- Recipe 38: Classic Beef Burger (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(38, 16, 5, 1), -- Ground Beef
(38, 26, 12, 4), -- Bread (burger buns)
(38, 27, 12, 2), -- Cheese
(38, 18, 12, 2), -- Tomato
(38, 19, 12, 4), -- Lettuce
(38, 6, 12, 4), -- Onion
(38, 1, 3, 1), -- Salt
(38, 2, 3, 0.5); -- Black Pepper

-- Recipe 39: Fresh Caesar Salad (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(39, 58, 13, 2), -- Lettuce
(39, 59, 1, 0.5), -- Croutons
(39, 60, 1, 0.25), -- Caesar Dressing
(39, 29, 1, 0.25), -- Parmesan Cheese
(39, 30, 13, 1); -- Lemon

-- Recipe 40: Fluffy Blueberry Muffins (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(40, 7, 1, 2), -- Flour
(40, 8, 1, 0.75), -- Sugar
(40, 10, 3, 2), -- Baking Powder
(40, 1, 3, 0.5), -- Salt
(40, 13, 1, 1), -- Milk
(40, 12, 13, 1), -- Eggs
(40, 4, 2, 4), -- Butter
(40, 55, 1, 1); -- Blueberries

-- Recipe 41: Classic French Toast (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(41, 26, 12, 8), -- Bread
(41, 12, 13, 4), -- Eggs
(41, 13, 1, 0.5), -- Milk
(41, 43, 3, 1), -- Vanilla Extract
(41, 38, 3, 1), -- Cinnamon
(41, 4, 2, 2); -- Butter

-- Recipe 42: Perfect Grilled Cheese (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(42, 26, 12, 4), -- Bread
(42, 27, 12, 4), -- Cheese
(42, 4, 2, 2); -- Butter

-- Recipe 43: Fresh Garden Salad (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(43, 58, 13, 4), -- Lettuce
(43, 18, 13, 2), -- Tomato
(43, 19, 13, 1), -- Bell Pepper
(43, 20, 13, 2), -- Carrot
(43, 21, 13, 2), -- Celery
(43, 6, 12, 1), -- Onion
(43, 3, 2, 2), -- Olive Oil
(43, 47, 2, 1); -- Vinegar

-- Recipe 44: Savory Rice Pilaf (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(44, 23, 1, 1.5), -- Rice
(44, 61, 1, 3), -- Vegetable Broth
(44, 6, 12, 1), -- Onion
(44, 5, 11, 2), -- Garlic
(44, 4, 2, 2), -- Butter
(44, 1, 3, 1), -- Salt
(44, 2, 3, 0.5); -- Black Pepper

-- Recipe 45: Homemade Garlic Bread (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(45, 26, 13, 1), -- Bread
(45, 4, 2, 4), -- Butter
(45, 5, 11, 4), -- Garlic
(45, 33, 2, 2), -- Parsley
(45, 1, 3, 0.5); -- Salt

-- Recipe 46: Hearty Vegetable Soup (duplicate entry)
INSERT OR IGNORE INTO RecipeIngredient (ri_recipe_id, ri_ingredient_id, ri_unit_type_id, ri_quantity) VALUES
(46, 61, 1, 6), -- Vegetable Broth
(46, 18, 13, 3), -- Tomato
(46, 20, 13, 2), -- Carrot
(46, 21, 13, 2), -- Celery
(46, 6, 12, 1), -- Onion
(46, 5, 11, 3), -- Garlic
(46, 22, 13, 2), -- Potato
(46, 1, 3, 1), -- Salt
(46, 2, 3, 0.5); -- Black Pepper

-- Instructions for the additional duplicate recipes
-- Recipe 37: Simple Grilled Chicken Breast
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(37, 1, 'Season chicken breast with salt, pepper, and minced garlic.'),
(37, 2, 'Brush with olive oil and let marinate for 15 minutes.'),
(37, 3, 'Preheat grill to medium-high heat.'),
(37, 4, 'Grill chicken 6-7 minutes per side until internal temp reaches 165°F.'),
(37, 5, 'Let rest 5 minutes before slicing.'),
(37, 6, 'Serve hot with your favorite sides.');

-- Recipe 38: Classic Beef Burger
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(38, 1, 'Form ground beef into 4 equal patties, season with salt and pepper.'),
(38, 2, 'Preheat grill or skillet to medium-high heat.'),
(38, 3, 'Cook patties 4-5 minutes per side for medium doneness.'),
(38, 4, 'Add cheese in last minute of cooking if desired.'),
(38, 5, 'Toast burger buns lightly.'),
(38, 6, 'Assemble burgers with lettuce, tomato, onion, and condiments.');

-- Recipe 39: Fresh Caesar Salad
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(39, 1, 'Wash and chop romaine lettuce into bite-sized pieces.'),
(39, 2, 'Place lettuce in large salad bowl.'),
(39, 3, 'Add Caesar dressing and toss to coat evenly.'),
(39, 4, 'Sprinkle with grated Parmesan cheese.'),
(39, 5, 'Top with croutons just before serving.'),
(39, 6, 'Serve immediately with lemon wedges.');

-- Recipe 40: Fluffy Blueberry Muffins
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(40, 1, 'Preheat oven to 375°F and line muffin tin with paper liners.'),
(40, 2, 'Mix flour, sugar, baking powder, and salt in large bowl.'),
(40, 3, 'Whisk together milk, egg, and melted butter.'),
(40, 4, 'Combine wet and dry ingredients until just mixed.'),
(40, 5, 'Gently fold in blueberries.'),
(40, 6, 'Fill muffin cups 2/3 full and bake 20-25 minutes until golden.');

-- Recipe 41: Classic French Toast
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(41, 1, 'Whisk together eggs, milk, vanilla, and cinnamon.'),
(41, 2, 'Heat butter in large skillet over medium heat.'),
(41, 3, 'Dip bread slices in egg mixture, coating both sides.'),
(41, 4, 'Cook in skillet 2-3 minutes per side until golden brown.'),
(41, 5, 'Serve hot with maple syrup and powdered sugar.'),
(41, 6, 'Keep warm in 200°F oven if making large batches.');

-- Recipe 42: Perfect Grilled Cheese
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(42, 1, 'Butter one side of each bread slice.'),
(42, 2, 'Place cheese between bread, buttered sides out.'),
(42, 3, 'Heat skillet over medium heat.'),
(42, 4, 'Cook sandwich 2-3 minutes per side until golden and crispy.'),
(42, 5, 'Press down gently with spatula while cooking.'),
(42, 6, 'Cut diagonally and serve immediately.');

-- Recipe 43: Fresh Garden Salad
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(43, 1, 'Wash and dry all vegetables thoroughly.'),
(43, 2, 'Chop lettuce, tomatoes, bell pepper, and onion.'),
(43, 3, 'Grate or julienne carrots and chop celery.'),
(43, 4, 'Combine all vegetables in large salad bowl.'),
(43, 5, 'Whisk together olive oil and vinegar for dressing.'),
(43, 6, 'Toss salad with dressing just before serving.');

-- Recipe 44: Savory Rice Pilaf
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(44, 1, 'Sauté diced onion and garlic in butter until fragrant.'),
(44, 2, 'Add rice and stir to coat with butter, toasting lightly.'),
(44, 3, 'Pour in vegetable broth and bring to a boil.'),
(44, 4, 'Reduce heat, cover, and simmer 18-20 minutes.'),
(44, 5, 'Let stand 5 minutes, then fluff with fork.'),
(44, 6, 'Season with salt and pepper, garnish with herbs.');

-- Recipe 45: Homemade Garlic Bread
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(45, 1, 'Preheat oven to 400°F.'),
(45, 2, 'Mix softened butter with minced garlic, parsley, and salt.'),
(45, 3, 'Slice bread horizontally and spread garlic butter evenly.'),
(45, 4, 'Wrap in foil or place cut-side up on baking sheet.'),
(45, 5, 'Bake 10-12 minutes until heated through and crispy.'),
(45, 6, 'Slice and serve immediately while hot.');

-- Recipe 46: Hearty Vegetable Soup
INSERT OR IGNORE INTO RecipeInstruction (recipe_id, step_number, instruction_text) VALUES
(46, 1, 'Sauté diced onion, garlic, carrots, and celery until softened.'),
(46, 2, 'Add diced tomatoes and cook 2-3 minutes.'),
(46, 3, 'Pour in vegetable broth and bring to a boil.'),
(46, 4, 'Add cubed potatoes and simmer 15-20 minutes until tender.'),
(46, 5, 'Season with salt, pepper, and herbs to taste.'),
(46, 6, 'Serve hot with crusty bread or crackers.');


from flask import Flask
from model import Recipes, Ingredient, db, connect_to_db
from server import app



def seed():
    db.drop_all()
    db.create_all()

    try:
        # Insert data into the tables
        recipes_data = [
    {
        "name": "Sweet and Sour Chicken",
        "instructions": "1. In a large non-stick skillet, heat oil over medium high heat. Season chicken (chopped) and add to pan. Brown chicken and remove to plate.<br> 2. Add red and green peppers and cook for 1 minute. Stir in pineapple chunks, juice, sugar, vinegar, and chicken stock and bring to a simmer. Simmer until sauce begins to reduce. Stir in cornstarch mixture and bring liquid to a simmer. Stir in chicken and cook for 5 minutes.<br> Serve over rice."
    },
    {
        "name": "French Dip Sandwiches",
        "instructions": "1. In a large, shallow skillet over moderate heat, melt butter. Add shallots to butter and sauté 2 minutes. Add flour to butter and shallot and cook a minute longer. Whisk in consommé in a slow stream. Bring sauce to a bubble and allow to simmer over heat until ready to serve.<br> 2. Pile meat loosely across your cutting board or a large work surface. Season meat with seasoning.<br> Assemble using a pair of kitchen tongs, dip meat into loose au jus sauce and pile into rolls. Serve with au jus dipping sauce."
    },
    {
        "name": "Good Old Fashioned Pancakes",
        "instructions": "1. In a large bowl, sift together the flour, baking powder, salt, and sugar. Make a well in the center and pour in the milk, egg, and melted butter. Mix until smooth.<br>  2. Heat a lightly oiled griddle or frying pan over medium-high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake. Brown on both sides and serve hot.<br>  Makes about 8 pancakes."
    },
    {
        "name": "Creamy Homemade baked Mac and Cheese",
        "instructions": "1. Preheat oven to 325 degrees F and grease a 3 qt baking dish (9x13). Set aside.<br> 2. Bring a large pot of salted water to a boil. When boiling, add dried pasta and cook 1 minute less than the package directs for al dente. Drain and drizzle with a little bit of olive oil to keep from sticking.<br> 3. While water is coming up to a boil, grate cheeses and toss together to mix, then divide into three piles. Approximately 3 cups for the sauce, 1 1/2 cups for the inner layer, and 1 1/2 cups for the topping.<br> 4. Melt butter in a large saucepan over medium heat. Sprinkle in flour and whisk to combine. Mixture will look like very wet sand. Cook for approximately 1 minute, whisking often. Slowly pour in about 2 cups of the milk/cream, while whisking constantly, until smooth. Slowly pour in the remaining milk/cream, while whisking constantly, until combined and smooth.<br> 5. Continue to heat over medium heat, whisking very often, until thickened to a very thick consistency. It should almost be the consistency of a semi-thinned out condensed soup.<br> 6. Stir in spices and 1 1/2 cups of the cheeses, stirring to melt and combine. Stir in another 1 1/2 cups of cheese, and stir until completely melted and smooth.<br> 7. In a large mixing bowl, combine drained pasta with cheese sauce, stirring to combine fully. Pour half of the pasta mixture into the prepared baking dish. Top with 1 1/2 cups of grated cheeses, then top that with the remaining pasta mixture.<br> 8. Sprinkle the top with the last 1 1/2 cups of cheese and bake for 15 minutes, until cheesy is bubbly and lightly golden brown."
    },
    # Add more recipes if needed
]

        for recipe in recipes_data:
            db.session.add(Recipes(**recipe))

        ingredients_data = [
            {"recipe_id": 1, "ingredient_name": "Vegetable Oil", "unit": "tbs", "measurement": "2"},
            {"recipe_id": 1, "ingredient_name": "Chicken Breasts", "unit": "lb", "measurement": "1"},
            {"recipe_id": 1, "ingredient_name": "Salt", "unit": "tsp", "measurement": "1/2"},
            {"recipe_id": 1, "ingredient_name": "Pepper", "unit": "tsp", "measurement": "1/2"},
            {"recipe_id": 1, "ingredient_name": "Red pepper chopped", "unit": "cup", "measurement": "1/2"},
            {"recipe_id": 1, "ingredient_name": "Cornstarch", "unit": "tsp", "measurement": "4"},
            {"recipe_id": 1, "ingredient_name": "Water", "unit": "tsp", "measurement": "4"},
            {"recipe_id": 1, "ingredient_name": "Canned Pineapple chuncks, drained", "unit": "cup", "measurement": "1"},
            {"recipe_id": 1, "ingredient_name": "Pineapple juice from can", "unit": "cup", "measurement": "1"},
            {"recipe_id": 1, "ingredient_name": "Brown sugar", "unit": "tbs", "measurement": "3"},
            {"recipe_id": 1, "ingredient_name": "Rice Vinegar", "unit": "tbs", "measurement": "3"},
            {"recipe_id": 1, "ingredient_name": "Chicken stock", "unit": "cup", "measurement": "1/4"},
            {"recipe_id": 1, "ingredient_name": "Green pepper chopped", "unit": "cup", "measurement": "1/2"},
            {"recipe_id": 1, "ingredient_name": "Cooked rice", "unit": "cup", "measurement": "4"},
            {"recipe_id": 2, "ingredient_name": "Butter", "unit": "tbs", "measurement": "3"},
            {"recipe_id": 2, "ingredient_name": "Shallot chopped", "unit": "qt", "measurement": "2"},
            {"recipe_id": 2, "ingredient_name": "All-purpose flour", "unit": "tbs", "measurement": "1"},
            {"recipe_id": 2, "ingredient_name": "Cans of Beef Consomme or Broth", "unit": "qt", "measurement": "3"},
            {"recipe_id": 2, "ingredient_name": "Deli sliced roast beef", "unit": "lb", "measurement": "1 1/2"},
            {"recipe_id": 2, "ingredient_name": "Steak Seasoning Blend or Salt and Pepper", "unit": "tsp", "measurement": "2"},
            {"recipe_id": 2, "ingredient_name": "Torpedo sandwich rolls", "unit": "qt", "measurement": "1"},
            {"recipe_id": 3, "ingredient_name": "All-purpose flour", "unit": "cups", "measurement": "2"},
            {"recipe_id": 3, "ingredient_name": "Baking powder", "unit": "tsp", "measurement": "4"},
            {"recipe_id": 3, "ingredient_name": "Salt", "unit": "tsp", "measurement": "1"},
            {"recipe_id": 3, "ingredient_name": "White sugar", "unit": "tbs", "measurement": "1"},
            {"recipe_id": 3, "ingredient_name": "Milk", "unit": "cup", "measurement": "1 3/4"},
            {"recipe_id": 3, "ingredient_name": "Egg", "unit": "qt", "measurement": "1"},
            {"recipe_id": 3, "ingredient_name": "Butter melted", "unit": "tbs", "measurement": "3"},
            {"recipe_id": 4, "ingredient_name": "Dried elbow pasta", "unit": "lb", "measurement": "1"},
            {"recipe_id": 4, "ingredient_name": "Butter", "unit": "qt", "measurement": "1 stick"},
            {"recipe_id": 4, "ingredient_name": "All purpose flour", "unit": "cup", "measurement": "1/2"},
            {"recipe_id": 4, "ingredient_name": "Milk", "unit": "cup", "measurement": "1 1/2"},
            {"recipe_id": 4, "ingredient_name": "Heavy Cream", "unit": "cup", "measurement": "2 1/2"},
            {"recipe_id": 4, "ingredient_name": "Grated Cheddar Cheese or equivalent", "unit": "cup", "measurement": "4"},
            {"recipe_id": 4, "ingredient_name": "Grated Swiss cheese", "unit": "cup", "measurement": "2"},
            {"recipe_id": 4, "ingredient_name": "Garlic Salt", "unit": "tbs", "measurement": "1"},
            {"recipe_id": 4, "ingredient_name": "Garlic Powder", "unit": "tbs", "measurement": "1"},
            {"recipe_id": 4, "ingredient_name": "Black Pepper", "unit": "tsp", "measurement": "1/2"},
            {"recipe_id": 4, "ingredient_name": "Paprika", "unit": "tsp", "measurement": "1/2"}
        ]
        for ingredient in ingredients_data:
            db.session.add(Ingredient(**ingredient))

        db.session.commit()
        print("DB has been seeded")
        
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")


if __name__ == '__main__':
    connect_to_db(app)
    seed()
  
    print("Database dropped and recreated.")

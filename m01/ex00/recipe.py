class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if not isinstance(name, str):
            raise TypeError("Name shoudl be a string")
        if not isinstance(cooking_lvl, int):
            raise TypeError("Cooking level must be an int")
        if cooking_lvl > 5 or cooking_lvl < 1:
            raise ValueError("Cooking level must be between 1 and 5")
        if not isinstance(cooking_time, int):
            raise TypeError("Cooking time should be an int")
        if cooking_time <= 0:
            raise ValueError("Cooking time should be strictly positive")
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients should be given as a list")
        if not all(isinstance(x, str) for x in ingredients):
            raise TypeError("Each ingredients should be a string")
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type sould be a string")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type is incorrect")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Returns the string to print with the recipe’s info"""
        txt = f"{self.name} {self.recipe_type} recipe.\n"
        txt += f"Level {self.cooking_lvl} for {self.cooking_time} minutes\n"
        txt += "Ingredients: " + " ".join(self.ingredients)
        txt += f"\nDescription: {self.description}"
        return txt


tourte = Recipe("Tourte", 3, 25, ["Water", "Mushrooms", "Flour"],
                "A beautiful tourte homemade", "lunch")
to_print = str(tourte)
print(to_print)

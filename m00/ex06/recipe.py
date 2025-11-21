cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 60
    }
}


def print_cookbook():
    for r in cookbook:
        print(r)


def print_recipe(name):
    if (name in cookbook):
        print(cookbook[name])
    else:
        print("Recipe not in cookbook")


def delete_recipe(name):
    if (name in cookbook):
        del cookbook[name]
        print(f"Recipe {name} correctly deleted")
    else:
        print("Recipe not in cookbook")


def add_recipe():
    key = input("Enter a name:\n")
    ingredients = []
    answer = input("Enter ingredients:\n")
    while True:
        if not answer:
            break
        ingredients.append(answer)
        answer = input("")
    meal = input("Enter a meal type:\n")
    while True:
        prep_time = input("Enter a preparation time:\n")
        if not prep_time.isnumeric():
            print("Wrong input")
        else:
            break
    cookbook[key] = {"ingredients": ingredients,
                     "meal": meal, "prep_time": prep_time}

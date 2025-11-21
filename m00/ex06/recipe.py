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


def print_recipe():
    try:
        name = input("Please enter a recipe name to get its details\n")
        if (name in cookbook):
            print(cookbook[name])
        else:
            print("Recipe not in cookbook")
    except EOFError:
        print("Eof. No print")


def delete_recipe():
    try:
        name = input("Please enter a recipe name to delete it\n")
        if (name in cookbook):
            del cookbook[name]
            print(f"Recipe {name} correctly deleted")
        else:
            print("Recipe not in cookbook")
    except EOFError:
        print("Eof. No delete")


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
            print("Numeric input only")
        elif int(prep_time) <= 0:
            print("Strictly positive number only")
        else:
            prep_time = int(prep_time)
            break
    cookbook[key] = {"ingredients": ingredients,
                     "meal": meal, "prep_time": prep_time}


def nice_quit():
    print("Closing phonebook. Bye Bye!")
    exit(0)


options = ["Add a recipe", "Delete a recipe",
           "Print a recipe", "Print the cookbook", "Quit"]
function = [add_recipe, delete_recipe, print_recipe, print_cookbook, nice_quit]
print("Welcome to the Python Cookbook!")
while True:
    print("\nList of avalaible options:")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")
    print("")
    try:
        while True:
            answer = input("Please select an option:\n")
            if answer.isnumeric():
                break
            print("Please, choose option with index number\n\n")
        function[int(answer) - 1]()
    except EOFError:
        nice_quit()

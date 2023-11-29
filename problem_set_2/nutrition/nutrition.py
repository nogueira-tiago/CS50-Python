def get_fruit_calories(fruit):
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloipe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80
    }

    fruit_lower = fruit.lower()

    if fruit_lower in fruit_calories:
        return fruit_calories[fruit_lower]

def main():
    user_fruit = input("Fruit: ")
    calories = get_fruit_calories(user_fruit)

    if calories is not None:
        print(f"Calories: {calories}.")
    else:
        print("This fruit is not in owr sistem, sorry.")

main()

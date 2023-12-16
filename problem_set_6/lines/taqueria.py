def item_price(item):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    item_capitalize = item.capitalize()

    if item_capitalize in menu:
        return menu[item_capitalize]
    else:
        return None

def main():
    total_cost = 0.0
    try:
        while True:
            item = input("Item: ")
            cost = item_price(item)

            if cost is not None:
                total_cost += cost
                print(f"Item cost:${cost:.2f}.")
            else:
                print("Item not on menu.")
    except EOFError:
        print(f"Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

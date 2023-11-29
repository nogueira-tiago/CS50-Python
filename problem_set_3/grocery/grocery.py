def main():
    grocery_list = {}

    try:
        while True:
            item = input("")
            if item is not None:
                item_lower = item.lower()
                grocery_list[item_lower] = grocery_list.get(item_lower, 0) + 1
            else:
                break
    except EOFError:
        sorted_items = sorted(grocery_list.keys())

        for item in sorted_items:
            count = grocery_list[item]
            print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()

def calculate_change(amount_inserted, amount_due):
    return amount_inserted - amount_due


def insert_coin():
    amount_due = 50
    amount_inserted = 0



    while amount_inserted < amount_due:
        coin = int(input("Insert coin: (25, 10 or 5 cents)"))
        if coin in [25,10,5]:
            amount_inserted += coin
            print(f"Amount due: {amount_inserted}")

    change = calculate_change(amount_inserted, amount_due)
    print(f"your change is: {change}")

insert_coin()
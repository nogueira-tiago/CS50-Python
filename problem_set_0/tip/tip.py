def main():
    dollars = dollars_to_float(input("how much was the meal ? "))
    percentage = percent_to_float(input("what percentage would you like to tip ?"))
    tip = dollars * percentage/100
    print(f"leave${tip:.2f}")

def dollars_to_float(d):
    dollar = float(d.lstrip("$"))
    return dollar

def percent_to_float(p):
    percent = float(p.rstrip("%"))
    return percent

main()

from validator_collection import checkers

def main():
    result = checkers.is_email(input("What is your email adress? "))
    if result:
        print("Valid")
    else:
        print("Invalid")

main()
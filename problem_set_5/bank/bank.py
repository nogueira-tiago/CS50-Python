def main():
    greeting = input("Greeting: ").lower().lstrip()

    message = confirmation(greeting)

    if message == "$ 0":
        print(f"{message}")
    elif message == "$ 20":
        print(f"{message}")
    elif message == "$ 100":
        print(f"{message}") 
        
def confirmation(greeting):
    amount_printed = "$ "

    if greeting.startswith("hello"):
        amount_printed += "0"
    elif greeting.startswith("h"):
        amount_printed += "20"
    else :
        amount_printed += "100"
    
    return amount_printed



if __name__ == "__main__":
    main()

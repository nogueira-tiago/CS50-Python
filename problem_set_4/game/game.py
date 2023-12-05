import random

def main():
    while True: 
        level = int(input("Level: ")) 
        if level >0:
            break
    random_number = random.randint(1,level)

    while True:
        number = int(input("Guess: "))
        if number > random_number:
            print("Too large!")
        elif number < random_number:
            print("Too small!")
        elif number == random_number:
            print("Just right!")
            break
            
if __name__ == "__main__":
    main()
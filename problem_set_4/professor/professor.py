import random

def main():
    level = get_level()
    count = 0
    for _ in range(10):
        x, y = generate_numbers(level)
        answer = input(f"{x} + {y} = ")
        if int(answer) == x + y:
            count += 1
        else:
            print("EEE")
    print(f"Score: {count}")

def get_level():
    while True:
        level = input("Level: (1, 2 or 3)")
        if level.isdigit() and int(level) in {1,2,3}:
            return int(level) 
        else:
            print("Invalid level!")   

def generate_numbers(level):
    if level not in {1,2,3}:
        raise ValueError("Invalid level!")
    
    min_value = 10** (level-1)
    max_value = 10** level-1
    return random.randint(min_value,max_value),random.randint(min_value,max_value)



if __name__ == "__main__":
    main()
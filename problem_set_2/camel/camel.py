def camel_to_snake(variable_name):
    snake_case_name = ""

    for character in variable_name:
        if character.isupper():
             snake_case_name += "_" + character.lower()
        else:
             snake_case_name += character
    return snake_case_name

def main():
    camel_case_name = input("Enter variable in camel case: ")

    snake_case_name = camel_to_snake(camel_case_name)

    print(f"In snake_case is {snake_case_name}")

main()

import emojize

def converter(input_text):
    mensage = emojize.emojize(input_text)
    return mensage

def main():
    user_input = input("Input: ")
    final = converter(user_input)
    print(f"Output: {final}")

if __name__ == "__main__":
    main()
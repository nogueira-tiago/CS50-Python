def main():
    string_normal = input("What is your message ? ")

    string_twttr = (message_twttr(string_normal))

    print(f"Your message in twttr is: {string_twttr}")
    
def message_twttr(message):
    string_input = ""
    vowels = "aeiouAEIOU"
    for character in message:
        if character.lower() in vowels:
            string_input += ""
        else:
            string_input += character
    return string_input


if __name__ == "__main__":
    main()
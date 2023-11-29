def message_twtrr(message):
    string_input = ""
    vowels = "aeiouAEIOU"
    for character in message:
        if character.lower() in vowels:
            string_input += ""
        else:
            string_input += character
    return string_input

def main():
    string_normal = input("What is your message ? ")

    string_twttr = (message_twtrr(string_normal))

    print(f"Your message in twttr is: {string_twttr}")

main()

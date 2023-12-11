def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def start_with_letters(s):
    return s[0:2].isalpha()

def valid_length(s):
    return 2 <= len(s) <= 6

def numbers_at_end(s):
    return s[-1].isdigit() and s[0].isalpha() and (s[2:].isdigit() or s[3:].isdigit()) and s[1] != '0'

def no_ponctuation(s):
    return all(char.isalnum() for char in s)

def is_valid(s):
    return start_with_letters(s) and valid_length(s) and numbers_at_end(s) and no_ponctuation(s)

if __name__ == "__main__":
    main()

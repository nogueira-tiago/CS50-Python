import re

def main():
    user_input = input("Text: ")
    try:
        result = count(user_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

def count(text):
    pattern = r"\bum\b"
    findall = re.findall(pattern, text, re.IGNORECASE)

    return len(findall)

if __name__ == "__main__":
    main()
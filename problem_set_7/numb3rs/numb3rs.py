import re

def main():
    ip_input = input("IPv4 Address: ")
    if validate(ip_input):
        print("True")
    else:
        print("False")

def validate(ip):
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")

    if pattern.match(ip):
        parts = map(int, ip.split("."))
        if all(0 <= part <= 255 for part in parts):
            return True
    return False     

if __name__ == "__main__":
    main()

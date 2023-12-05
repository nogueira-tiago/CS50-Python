import inflect
p = inflect.engine()

def main():
    name_list = []
    try:
        while True:
            name = input("Name: ")
            name_list.append(name)
    except EOFError:
        joined_list = p.join(name_list)
        print(f"Adieu, adieu, to {joined_list}")    

if __name__ == "__main__":
    main()
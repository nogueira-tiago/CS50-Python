def calculate_percentage(fraction):
     x, y = fraction.split("/")
     x = int(x)
     y = int(y)
     percentage = ((x/y)*100)

     if percentage > 99:
         return "F"
     elif percentage < 1:
         return "E"
     else:
         return round(percentage)

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(f"{calculate_percentage(fraction)}%")
            break
        except ValueError:
            print("This isn't a number, try again.")
        except ZeroDivisionError:
            print("Dividing by zero is inconclusive.")

if __name__ == "__main__":
  main()
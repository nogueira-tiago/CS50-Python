import requests
import sys

def main():
    try:
        while True:
            if sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
                if len(sys.argv) != 2:
                    print("Insert only 1 argument")
                else:
                    number = sys.argv[1]
                    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout = 0.5) 
                    object = response.json()
                    rate = float(object["bpi"]["USD"]["rate"].replace(",", "").replace(" ", "").replace("USD", ""))
                    amount = rate * int(number)
                    print(f"{amount:,.4f}")
                    break
            else:
                print("It's not a number")
    except requests.RequestException:
        print("Error with the request,try another time.")

if __name__ == "__main__":
    main()
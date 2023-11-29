def month_is_valid(month):
    months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
    ]

    return month in months

def convert_date(input_date):
    parts = input_date.split()

    if len(parts)==3:
        month, day, year = parts
        if month_is_valid(month) and day.isdigit() and year.isdigit():
            return f"{year.zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    elif len(parts) == 1:
        date_parts = parts[0].split('/')
        if len(date_parts) == 3 and all(part.isdigit() for part in date_parts):
            month, day, year = date_parts
            if month_is_valid(month):
                return f"{year.zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    return None



def main():
    while True:
        user_input = input("Date: ")

        formated_date = convert_date(user_input)

        if formated_date is not None:
            print(f"{formated_date}")
            break
        else:
            print("Invalid format,try again.")

if __name__ == "__main__":
   main()

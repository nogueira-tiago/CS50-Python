def main():
    time_str = input("What time is it ? ")
    time = convert(time_str)

    if 7 <= time <= 8:
        print("Breakfast time!")
    elif 12 <= time <= 13:
        print("Lunch time!")
    elif 18 <= time <= 19:
        print("Dinner time!")
    else:
        return None

def convert(timeString):
    hours , minutes = timeString.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()

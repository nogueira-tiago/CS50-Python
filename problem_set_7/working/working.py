import re

def main():
    input_time = input("Hours: ").lower()
    
    try:
        result = convert(input_time)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

def convert(time):
    time_pattern = r"^(\d{1,2}:\d{2}) (am|pm) to (\d{1,2}:\d{2}) (am|pm)$"
    match = re.search(time_pattern, time)

    if match:
        start_time, start_meridiem, end_time, end_meridiem = match.groups()
        start_hour, start_minute = [int(part) for part in start_time.split(":")]
        end_hour, end_minute = [int(part) for part in end_time.split(":")]

        if 0 <= start_hour <= 23 and 0 <= start_minute <= 59 and \
           0 <= end_hour <= 23 and 0 <= end_minute <= 59:

            if start_meridiem == "pm" and start_hour != 12:
                start_hour += 12
            if end_meridiem == "pm" and end_hour != 12:
                end_hour += 12
            
            if start_hour > end_hour or (start_hour == end_hour and start_minute > end_minute):
                raise ValueError("End time is starting before start time.")
            
            return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"
        
    raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()
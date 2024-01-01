from datetime import datetime
import inflect

def main():
    birth = input("Date of birth: ")
    
    try:
        result = days_to_min(birth)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

def days_to_min(birth):
    convert_str = datetime.strptime(birth, "%Y-%m-%d")
    convert_str = convert_str.replace(hour=0, minute=0, second=0, microsecond=0)
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    age_in_min = round((today - convert_str).total_seconds() / 60)
    age_words = convert_to_words(age_in_min)
    return age_words

def convert_to_words(minutes):
    p = inflect.engine()
    age_words = p.number_to_words(minutes)  
    age_words = age_words.replace(" and","")
    age_words += " minutes"

    return age_words

if __name__ == "__main__":
    main()

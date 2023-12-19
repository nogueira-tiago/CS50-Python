import sys
import csv
import os

def convert_csv(input_file, output_file):
    try:
        with open(input_file, "r") as input_csv, open(output_file, "w", newline="") as output_csv:
            reader =csv.DictReader(input_csv)
            fieldnames = ["first_name","last_name","house"]
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

            writer.writeheader()
        
            for row in reader:
                if len(row) !=2:
                    print("Usage: python scourgify.py <filename.csv> <outputfile.csv>")
                    sys.exit(1)

                full_name = row["name"].strip('"')
                house = row["house"]

                name_parts = full_name.split(',')
                if len(name_parts) != 2:
                    print(f"Error: Invalid name format in the input CSV: {row[0]}")

                
                first_name, last_name = name_parts

                writer.writerow({"first_name":first_name.strip(),"last_name":last_name.strip(),"house":house.strip()})
    
    except FileNotFoundError:
        print("Usage: python program.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

def find_file_path(directory, file_name):
    for root, dirs, files in os.walk(directory):
        if  file_name in files:
            return os.path.join(root, file_name)
    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    current_directory = os.getcwd()
    file_path = find_file_path(current_directory, input_file)

    if file_path is None:
         print(f"Error: File '{input_file}' not found")

    convert_csv(input_file, output_file)

if __name__ == "__main__":
    main()
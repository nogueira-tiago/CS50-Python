from tabulate import tabulate
import os
import sys
import csv

def formating(file_name):
    text = []
    with open(f"{file_name}") as file:
        reader = csv.reader(file)
        for row in reader:
            text.append({"Sicilian Pizza": row[0],"Small": row[1], "Large": row[2] })
        return text

def find_file_path(directory, file_name):
    for root, dirs, files in os.walk(directory):
        if  file_name in files:
            return os.path.join(root, file_name)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename.py")
        sys.exit(1)

    input_file = sys.argv[1]
    current_directory = os.getcwd()
    file_path = find_file_path(current_directory, input_file)

    if file_path is None:
         print(f"Error: File '{input_file}' not found")
    
    text_formated = formating(file_path)
    print(tabulate(text_formated,headers="firstrow",showindex="false",tablefmt="grid"))

if __name__ == "__main__":
    main()
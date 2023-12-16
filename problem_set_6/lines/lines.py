import sys
import os

def count_lines(file_path):
    try:
        with open(file_path) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

    code_lines = 0

    in_multipleline_coment = False
    for line in lines:
        stripped_line = line.strip()

        if  stripped_line.startswith("''") or stripped_line.startswith('""'):
            in_multipleline_coment = not in_multipleline_coment

        if not in_multipleline_coment and stripped_line and not stripped_line.startswith("#"):
            code_lines += 1
            
    return code_lines

def find_file_path(directory,file_name):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename.py>")
        sys.exit(1)

    input_file = sys.argv[1]
    current_directory = os.getcwd()
    file_path = find_file_path(current_directory, input_file)

    if file_path is None:
         print(f"Error: File '{input_file}' not found")

    lines_of_code = count_lines(file_path)
    print(f"{lines_of_code} lines.")

if __name__ == "__main__":
    main()

    
import os
import sys
from PIL import Image, ImageOps

def find_file_path(directory, file_name):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def paste_shirt(input_file, output_file, shirt_file):
    try:
        with Image.open(input_file) as input_png:
            with Image.open(shirt_file) as shirt_png:

                resized_input =ImageOps.fit(input_png, shirt_png.size)
                shirt = shirt_png.copy()
                resized_input.paste(shirt, shirt)
                resized_input.save(output_file)
        
    except FileNotFoundError:
        print(f"Image can't be read.")    

def main():
    if len(sys.argv) !=3 and len(sys.argv[1]) != len(sys.argv[2]):
        print("Usage: python shirt.py <input_file.png> <output_file.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    shirt_path = "shirt.png"
    current_directory = os.getcwd()
    file_path = find_file_path(current_directory, input_file)
    valid_extensions = {".jpg", ".jpeg", ".png"}

    if not (input_file.lower().endswith(tuple(valid_extensions)) and
            output_file.lower().endswith(tuple(valid_extensions))):
        print("Error: Invalid file extensions. Supported formats: JPG, JPEG, PNG.")
        sys.exit(1)

    if file_path is None:
        print(f"Error: file'{input_file}' not found")

    paste_shirt(input_file,output_file, shirt_path)

if __name__ == "__main__":
    main()
import fpdf
import os

pdf = fpdf.FPDF()
fixed_path = r"C:\Users\TIAGO MOURA\Documents\Estudos\CS50-Python\problem_set_8\shirtificate\shirtificate.png"

def find_file_path(directory, file_name):
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        return file_path
    return None

def get_name(user_name):
    name = user_name + " took CS50"
    pdf.set_font("helvetica", size=18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, -420, name, align = "C")


def set_image(image_path):
    pdf.image(image_path, w=210, h=297)

def merge(image, name):
    pdf.add_page("P","A4")
    set_image(image)
    image_height = pdf.get_y()
    pdf.set_y(image_height)
    get_name(name)
    
    pdf.output("ready_shirtificate.pdf")

if __name__ == "__main__":
    image_path = find_file_path(os.getcwd(), fixed_path)
    user_name = input("Name: ")
    merge(image_path, user_name)

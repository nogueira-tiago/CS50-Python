import random
import sys
import pyfiglet  

def random_font(): 
    fonts = pyfiglet.Figlet().getFonts()
    return random.choice(fonts)

def output_text(text,font):
    fig = pyfiglet.Figlet(font=font)
    result = fig.renderText(text)
    print(result)

def main():
    if len(sys.argv) < 2:
       font = random_font()
       font_name = font 
       sys.exit(1)
    elif len(sys.agrv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            print("Invalid usage.")
            sys.exit(1)
        font_name = sys.argv[2]
    print("Invalid usage.")
    
    user_input = input("Input: ")
    output_text(user_input,font_name)

if __name__ == "__main__":
    main()
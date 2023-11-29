def main ():
    extension = input("File name: ").lstrip().lower()

    if extension.endswith(".gif"):
        print("image/gif")
    elif extension.endswith(".jpeg"):
        print("image/jpeg")
    elif extension.endswith(".jpg"):
        print("image/jpeg")
    elif extension.endswith(".png"):
        print("image/png")
    elif extension.endswith(".pdf"):
        print("aplication/pdf")
    elif extension.endswith(".txt"):
        print("text/plain")
    elif extension.endswith(".zip"):
        print("aplication/zip")

main()

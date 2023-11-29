def convert(text):
  convertedText = text.replace(":)","🙂")
  convertedText = text.replace(":(","🙁")
  return convertedText

def main():
  final = convert(input())
  print(final)

main()

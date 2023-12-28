import re

def main():
    link = input("HTML: ")
    result = parse(link)

    if result:
        print(result)
    else:
        print("Error")

def parse(str):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    link_pattern = re.search(pattern, str)
    if link_pattern:
        video_id = link_pattern.group(1)
        return f'https://youtu.be/{video_id}'
    
    return None

if __name__ == "__main__":
    main()
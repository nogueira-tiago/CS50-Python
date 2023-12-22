import re

def main():
    link = input("HTML: ")
    print(parse(link))

def parse(str):
    link_pattern = re.search(r"^http(S)?://(www.)?youtube(\.com/.+)/(.+)", str)
    if link_pattern:
        grp1, grp2, grp3, grp4 = link_pattern.groups()
        final_link = f"http{grp1}://{grp2}youtu.be/{grp4}"
        return final_link
    return False

if __name__ == "__main__":
    main()
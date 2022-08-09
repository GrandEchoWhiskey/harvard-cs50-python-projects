def main():
    print(parse(input("HTML: ")))


def parse(s):

    try:
        link = s.split('src=\"')[1].split('\"')[0]

        if link.find("youtube") == -1:
            return None

        link = link.replace("http:", "https:").replace('embed/', '')
        return link.replace('www.youtube.com', 'youtu.be').replace('youtube.com', 'youtu.be')

    except:
        return None

if __name__ == "__main__":
    main()
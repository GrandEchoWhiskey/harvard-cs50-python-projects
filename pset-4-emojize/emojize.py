import emoji

def main():

    inp = input()

    print(emoji.emojize(inp, language='alias'))

    return

if __name__ == "__main__":
    main()
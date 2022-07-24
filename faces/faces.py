def convert(txt: list):

    for index, item in enumerate(txt):

        if item == ':)':
            txt[index] = '🙂'
            continue

        if item == ':(':
            txt[index] = '🙁'
            continue

    return txt

def main():
    sentence: list = input().split(' ')
    sentence = convert(sentence)
    for item in sentence:
        print(item, end=' ')
    print()

if __name__ == "__main__":
    main()
def main():
    inp = input("Input: ")
    print("Output: " + shorten(inp))

def shorten(word):
    rem = ['a', 'e', 'i', 'o', 'u']
    rem.extend([r.upper() for r in rem])

    for letter in rem:
        word = word.replace(letter, '')
    return word


if __name__ == "__main__":
    main()
def main():

    new_str = ""
    inp = input("camelCase: ")

    for char in inp:

        if char.isupper():
            new_str += '_' + char.lower()
            continue

        new_str += char

    print("snake_case: " + new_str)

    return


if __name__ == "__main__":
    main()
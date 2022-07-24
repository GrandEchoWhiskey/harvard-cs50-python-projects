def main():

    shopping_list: dict = {}

    while True:
        try:
            item = input().upper()
            if item in shopping_list.keys():
                shopping_list[item] += 1
                continue
            shopping_list[item] = 1
        except EOFError:
            print()
            for key in sorted(shopping_list.keys()):
                print(f"{shopping_list[key]} {key}")
            break

    return

if __name__ == "__main__":
    main()
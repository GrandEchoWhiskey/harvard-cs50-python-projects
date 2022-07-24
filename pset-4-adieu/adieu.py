def main():

    names = []

    while True:

        try:

            names.append(input("Name: "))

        except:
            break

    res_str = ""

    for index, name in enumerate(names):

        if index == 0:
            res_str += f"Adieu, adieu, to {name}"
            continue

        if index == len(names)-1:
            if len(names) > 2:
                res_str += ','
            res_str += f" and {name}"
            continue

        res_str += f", {name}"
        continue

    print(res_str)

    return

if __name__ == "__main__":
    main()
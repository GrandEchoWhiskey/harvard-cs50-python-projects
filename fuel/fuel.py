def main():

    f: float

    while True:
        try:
            inp = input("Fraction: ").split('/')
            f = float(eval(f"{int(inp[0])}/{int(inp[1])}"))
            if f > 1:
                continue
        except:
            continue
        break

    f *= 100
    if f >= 99:
        print("F")
        return
    if f <= 1:
        print("E")
        return

    print(str(round(f)) + "%")
    return

if __name__ == "__main__":
    main()
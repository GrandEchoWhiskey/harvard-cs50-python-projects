def main():
    inp = input("Fraction: ")
    print(gauge(convert(inp)))


def convert(fraction: str):

    if int(fraction.split('/')[1]) == 0:
        raise ZeroDivisionError

    if int(fraction.split('/')[0]) > int(fraction.split('/')[1]):
        raise ValueError

    return int(round(float(eval(fraction)) * 100))

def gauge(percentage: int):

    if percentage >= 99:
        return "F"

    if percentage <= 1:
        return "E"

    return str(percentage) + '%'


if __name__ == "__main__":
    main()

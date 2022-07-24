alpha = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
digit = [str(x) for x in range(10)]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha_allowed = True

    if len(s) < 2 or len(s) > 6:
        return False

    for char in s:

        if not (char in alpha or char in digit):
            return False

    if not (s[0] in alpha or s[1] in alpha):
        return False

    for i in range(len(s)):

        if s[i] in digit and alpha_allowed:

            if s[i] == '0':
                return False

            alpha_allowed = False
            continue

        if s[i] in alpha and not alpha_allowed:
            return False

    return True


main()
def main():
    print(count(input("Text: ")))


def count(s):
    alnum = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    alnum.extend([x.upper for x in alnum])
    alnum.extend(str(x) for x in range(10))

    s = s.lower()

    ci = 0
    count = 0

    if s[0:2] == 'um':
        count += 1
        ci = 2

    while True:

        fi = s[ci:].find('um')

        if fi == -1:
            break

        try:
            if s[ci + fi - 1] in alnum or s[ci + fi + len('um')] in alnum:
                ci = ci + fi + len('um')
                continue
        except:
            count += 1
            break

        count += 1
        ci = ci + fi + len('um')

    return count


if __name__ == "__main__":
    main()
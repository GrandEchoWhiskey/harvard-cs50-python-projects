def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if len(ip.split('.')) != 4:
        return False

    octets = ip.split('.')

    try:

        for octet in octets:

            if int(octet) > 255 or int(octet) < 0:
                return False

    except:
        return False

    return True

if __name__ == "__main__":
    main()
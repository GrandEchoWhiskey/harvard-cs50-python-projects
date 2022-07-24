def main():

    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):

    greeting = greeting.lower()
    greeting = greeting.replace(' ', '')

    if len(greeting) == 0:
        return None

    if greeting[0] == 'h':

        if len(greeting) < 5:
            pass

        elif greeting[:5] == 'hello':
            return 0

        return 20

    return 100

if __name__ == "__main__":
    main()







if __name__ == "__main__":
    main()
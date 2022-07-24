def main():
    greeting = input("Greeting: ")
    greeting = greeting.lower()
    greeting = greeting.replace(' ', '')

    if len(greeting) == 0:
        return

    if greeting[0] == 'h':
        if len(greeting) < 5:
            pass
        elif greeting[:5] == 'hello':
            print("$0")
            return
        print("$20")
        return
    print("$100")
    return

if __name__ == "__main__":
    main()
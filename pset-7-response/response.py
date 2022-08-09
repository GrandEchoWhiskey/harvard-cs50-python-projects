from validator_collection import checkers

def main():

    if checkers.is_email(input("What's your email address? ")):
        return "Valid"

    return "Invalid"


if __name__ == "__main__":
    print(main())
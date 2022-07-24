import random


def main():

    level = get_level()

    score = 0

    for _ in range(10):

        words = [generate_integer(level) for _ in range(2)]
        result = sum(words)
        answer = None

        for try_ in range(3):

            print(f"{words[0]} + {words[1]} = ", end='')

            try:
                answer = int(input())
            except:
                answer = None

            if answer == result:
                break

            print("EEE")

        if answer == result:
            score += 1
            continue

        print(f"{words[0]} + {words[1]} = {result}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            res = int(input("Level: "))
            if res not in range(1, 4):
                continue
            return res

        except:
            continue


def generate_integer(level):

    try:
        m = 10
        res = random.choice(range(m**(level - 1) if m**(level - 1) != 1 else 0, m**level))
        return res

    except:
        return generate_integer(level)


if __name__ == "__main__":
    main()
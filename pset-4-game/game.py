import random

def main():

    inp: int

    while True:

        try:

            inp = random.choice(range(1, int(input("Level: "))))
            break

        except:
            continue

    while True:

        try:

            ninp = int(input("Guess: "))
            if ninp == inp:
                print("Just right!")
                return
            if ninp < inp:
                print("Too small!")
                continue
            if ninp > inp:
                print("Too large!")
                continue

        except:
            continue

if __name__ == "__main__":
    main()
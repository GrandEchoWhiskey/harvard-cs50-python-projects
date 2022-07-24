from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

def main():

    if len(sys.argv) not in [1, 3]:
        sys.exit(1)

    f = random.choice(figlet.getFonts())

    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit(1)
        if sys.argv[2] not in figlet.getFonts():
            sys.exit(1)
        f = sys.argv[2]

    inp = input()

    figlet.setFont(font=f)

    print(figlet.renderText(inp))

    sys.exit(0)

if __name__ == "__main__":
    main()
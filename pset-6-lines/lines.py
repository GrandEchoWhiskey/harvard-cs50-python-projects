import sys

err_no = [
    "Too few command-line arguments",
    "Too many command-line arguments",
    "Not a Python file",
    "File does not exist"
]

def is_py_file(filename: str):

    if len(filename.split('.')) < 2:
        return False

    if filename.split('.')[-1] != 'py':
        return False

    return True

def calculate(filename: str):

    count: int = 0
    f = open(filename, "r")

    for line in f:

        formatted = line.replace('\n', '').replace(' ', '')

        if formatted == '':
            continue

        if formatted[0] == '#':
            continue

        count += 1

    f.close()
    return count

def main():

    if len(sys.argv) < 2:
        sys.exit(err_no[0])

    if len(sys.argv) > 2:
        sys.exit(err_no[1])

    if not is_py_file(sys.argv[1]):
        sys.exit(err_no[2])

    try:
        print(calculate(sys.argv[1]))

    except:
        sys.exit(err_no[3])

    sys.exit(0)

if __name__ == "__main__":
    main()
from tabulate import tabulate
import sys

err_no = [
    "Too few command-line arguments",
    "Too many command-line arguments",
    "Not a CSV file",
    "File does not exist"
]

def is_csv_file(filename: str):

    if len(filename.split('.')) < 2:
        return False

    if filename.split('.')[-1] != 'csv':
        return False

    return True

def format_(filename: str):

    f = open(filename, 'r')
    h: list
    t: list = []
    for i, line in enumerate(f):
        row: list = line.replace('\n', '').split(',')
        if not i:
            h = row
            continue
        t.append(row)

    f.close()

    return tabulate(t, h, tablefmt="grid")

def main():

    if len(sys.argv) < 2:
        sys.exit(err_no[0])

    if len(sys.argv) > 2:
        sys.exit(err_no[1])

    if not is_csv_file(sys.argv[1]):
        sys.exit(err_no[2])

    try:
        print(format_(sys.argv[1]))

    except:
        sys.exit(err_no[3])

    sys.exit(0)

if __name__ == "__main__":
    main()

import sys
import csv

err_no = [
    "Too few command-line arguments",
    "Too many command-line arguments",
    "Could not read "
]

def scourgify(filenames):

    csv_r = open(filenames[0], "r")
    reader = csv.DictReader(csv_r, delimiter=",")

    csv_w = open(filenames[1], "w+")
    writer = csv.DictWriter(csv_w, fieldnames=["first", "last", "house"])

    writer.writeheader()

    for row in reader:
        last, first = row["name"].split(",")
        house = row["house"]

        writer.writerow(
            {"first": first.strip(), "last": last, "house": house}
        )

    csv_r.close()
    csv_w.close()

def main():

    if len(sys.argv) < 3:
        sys.exit(err_no[0])

    if len(sys.argv) > 3:
        sys.exit(err_no[1])

    try:
        scourgify(sys.argv[1:])

    except:
        sys.exit(err_no[2] + sys.argv[1])

    sys.exit(0)

if __name__ == "__main__":
    main()
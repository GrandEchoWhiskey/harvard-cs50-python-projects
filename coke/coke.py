COKE = 50

def main():

    inserted = 0

    while inserted < COKE:
        print("Amount Due: " + str(COKE - inserted))
        add = int(input("Insert Coin: "))
        if add not in [5, 10, 25]:
            continue
        inserted += add

    print("Change Owed: " + str(inserted - COKE))

    return

if __name__ == "__main__":
    main()
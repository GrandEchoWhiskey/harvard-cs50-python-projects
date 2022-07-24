C = 300000000

def main():
    try:
        m = int(input("m: "))
        E = m * (C ** 2)
        print("E: " + str(E))
    except:
        pass

if __name__ == "__main__":
    main()
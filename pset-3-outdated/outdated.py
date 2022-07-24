months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        try:
            inp = input("Date: ")

            if '/' in inp:
                if len(inp.split('/')) == 3:
                    spl = inp.split('/')
                    if int(spl[0]) <= 12 and int(spl[0]) > 0 and int(spl[1]) <= 31 and int(spl[1]) > 0 and int(spl[2]) > 0:
                        print(f"{int(spl[2]):04}-{int(spl[0]):02}-{int(spl[1]):02}")
                        return

            if len(inp.split(' ')) == 3:

                if ',' in inp:
                    n_inp = inp.replace(',', '')
                    spl = n_inp.split(' ')
                    if spl[0] in months and int(spl[2]) > 0 and int(spl[1]) <= 31 and int(spl[1]) > 0:
                        print(f"{int(spl[2]):04}-{int(months.index(spl[0])+1):02}-{int(spl[1]):02}")
                        return

                spl = inp.split(' ')
                if spl[1] in months and int(spl[2]) > 0 and int(spl[0]) <= 31 and int(spl[0]) > 0:
                    print(f"{int(spl[2]):04}-{int(months.index(spl[1])+1):02}-{int(spl[0]):02}")
                    return
        except:
            continue


if __name__ == "__main__":
    main()
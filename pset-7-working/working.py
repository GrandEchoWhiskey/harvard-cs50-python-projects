def main():
    print(convert(input("Hours: ")))

def get_time(s: str):
    if s.find(':') == -1:
        return (int(s), 0)
    return (int(x) for x in s.split(':'))

def check_time(h: int, m: int):
    if h > 12 or h < 0:
        return False
    if m > 59 or m < 0:
        return False
    return True

def convert(s: str):
    try:
        times = s.lower().split(' to ')

        for i, time in enumerate(times):
            h, m = get_time(time.split(' ')[0])

            if not check_time(h, m):
                raise Exception

            sf = time.split(' ')[1]

            if sf == 'pm' and h != 12:
                h += 12
                
            if sf == 'am' and h == 12:
                h = 0

            times[i] = f"{h:02}:{m:02}"

        return f"{times[0]} to {times[1]}"
    except:
        pass
    raise ValueError


if __name__ == "__main__":
    main()
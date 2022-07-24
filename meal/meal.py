def main():
    time = convert(input("What time is it? "))
    if time >= 7 and time <= 8:
        print("breakfast time")
        return
    if time >= 12 and time <= 13:
        print("lunch time")
        return
    if time >= 18 and time <= 19:
        print("dinner time")
        return


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return float(hours + (minutes / 60))


if __name__ == "__main__":
    main()
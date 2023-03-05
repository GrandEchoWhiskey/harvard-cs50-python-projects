def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        if d[0] == '$':
            d = d[1:]
        d = float(d)
    except:
        d = float(0)
    return d

def percent_to_float(p):
    try:
        if p[-1] == '%':
            p = p[:-1]
        p = float(p)/100
    except:
        p = float(0)
    return p

main()
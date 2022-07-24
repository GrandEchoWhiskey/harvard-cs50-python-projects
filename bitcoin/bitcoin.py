import requests
import sys

def main():

    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if r.status_code == 200:
            data = r.json()
            data = float(data['bpi']['USD']['rate'].replace(',', ''))
            data = data * float(sys.argv[1])
            print(f"${data:,.4f}")
    except:
        sys.exit(1)

    return

if __name__ == "__main__":
    main()
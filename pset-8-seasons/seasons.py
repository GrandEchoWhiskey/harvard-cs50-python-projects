import sys
import inflect
from datetime import datetime, date, timedelta

class BirthDate:
    def __init__(self, _date:str):
        self._p = inflect.engine()
        self._date:datetime = self.convert(_date)
        self._now:datetime = self.now()

    def __str__(self):
        words = self._p.number_to_words(self.min_delta(), andword="")
        words = f"{words} minutes".capitalize()
        return words

    def convert(self, str_date:str):
        try:
            return datetime.strptime(str_date.strip(), "%Y-%m-%d")

        except:
            sys.exit("Invalid Date")

    def now(self):
        return datetime.combine(date.today(), datetime.min.time())

    def min_delta(self):
        td = self._now - self._date
        time = int(td / timedelta(minutes=1))
        return time

def main():
    bd = BirthDate(input("Date of Birth: "))
    print(str(bd))

if __name__ == "__main__":
    main()
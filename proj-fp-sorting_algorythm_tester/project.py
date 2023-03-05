import random
from timeit import default_timer as timer
import sys
import importlib

LST_TYPES = ["sorted", "reversed", "random"]
IMPORTABLE = [
    "quicksort",
    "mergesort",
    "heapsort",
    "shellsort",
    "bubblesort"
]

class sorting:

    def __init__(self, lst: list, algorythm):
        self.__lst = lst
        self.__algorythm = algorythm
        self.__last_ms = 0

    def run(self):
        start = timer()
        self.__algorythm.sort(self.__lst)
        end = timer()
        self.__last_ms = (end-start) * 1000
        return self

    @property
    def time(self): return self.__last_ms

    @property
    def algorythm(self): return self.__algorythm

    @property
    def list(self): return self.__lst

def usage_note_exit():
    raise SystemExit("Usage: python project.py <sorted, reversed, random> length [*alogythms | all].")

def algorythm_modules(lst):
    algos = set()
    for arg in lst:
        if arg.lower() == "all":
            for imp in IMPORTABLE:
                algos.add(importlib.import_module(imp))
            break
        elif arg.lower() in IMPORTABLE:
            algos.add(importlib.import_module(arg.lower()))
    if len(algos) == 0: raise SystemExit("Algorythm modules not found.")
    return algos

def starting_list(typ, length):
    if typ == 0:
        return list(range(1, length+1))
    if typ == 1:
        return list(range(length, 0, -1))
    if typ == 2:
        return random.choices(range(1, length+1), k=length)

def main():

    if len(sys.argv) < 4:
        usage_note_exit()

    if sys.argv[1] not in LST_TYPES:
        usage_note_exit()

    try: length = int(sys.argv[2])
    except: usage_note_exit()

    algos = algorythm_modules(sys.argv[3:])
    lst = starting_list(LST_TYPES.index(sys.argv[1]), length)

    for algo in algos:
        try: print(f"{algo.__name__.capitalize()}: ", sorting(lst.copy(), algo).run().time)
        except RecursionError: print(f"{algo.__name__.capitalize()}: ", "Too much recursion to handle.")

if __name__ == '__main__':
    main()

# Shellsort

def sort(lst):

    n = len(lst)

    # Rearrange items at n/(2^x) starting from n/2
    interval = n // 2
    while interval > 0:

        for i in range(interval, n):
            tmp = lst[i]
            j = i

            while j >= interval and lst[j - interval] > tmp:
                lst[j] = lst[j - interval]
                j -= interval

            lst[j] = tmp

        interval //= 2
# Bubblesort

def __swap(lst: list, index_a: int, index_b: int):

    # Swap list items
    (lst[index_a], lst[index_b]) = (lst[index_b], lst[index_a])


def sort(lst: list):

    # Create loop for max swaps
    n = len(lst)
    for i in range(n - 1):

        # Loop from 0 to last correctly placed item
        swapped = False
        for j in range(n - i - 1):

            # If left bigger than right - swap
            if lst[j] > lst[j + 1]:
                swapped = True
                __swap(lst, j, j + 1)

        # If no swaps were done the array must be correctly sorted
        if not swapped:
            return
    
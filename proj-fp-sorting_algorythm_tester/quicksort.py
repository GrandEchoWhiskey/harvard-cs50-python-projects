# Quicksort

def __swap(lst: list, index_a: int, index_b: int):

    # Swap list items
    (lst[index_a], lst[index_b]) = (lst[index_b], lst[index_a])


def __partition(lst: list, left: int, right: int):

    # Swap middle with last item (Optional for sorted and reversed lists)
    __swap(lst, right, ((right-left)//2)+left)

    # Select pivot as last list item
    pivot = lst[right]

    # Loop through list and push lower to left
    i = left - 1
    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1
            __swap(lst, i, j)

    # Place pivot in his place
    __swap(lst, i + 1, right)
    return i + 1


def __quick(lst: list, left: int, right: int):

    # Stop recursion
    if left >= right: return

    # Partition around pivot
    pivot_index = __partition(lst, left, right)

    # Recursively sort left and right site
    __quick(lst, left, pivot_index - 1)
    __quick(lst, pivot_index + 1, right)


def sort(lst: list):

    # Run with initial range args
    __quick(lst, 0, len(lst) - 1)

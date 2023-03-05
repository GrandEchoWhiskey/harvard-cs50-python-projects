# Heapsort

def __swap(lst: list, index_a: int, index_b: int):

    # Swap list items
    (lst[index_a], lst[index_b]) = (lst[index_b], lst[index_a])


def __siftDown(lst, i, top):

    while True:

        # Set indexes
        left = i * 2 + 1
        right = i * 2 + 2

        # If 2 children
        if max(left, right) < top:

            # If parent is greater than child node end
            if lst[i] >= max(lst[left], lst[right]): break
            
            # Left node greater than right
            elif lst[left] > lst[right]:
                __swap(lst, i, left)
                i = left

            # Right node greater than left
            else:
                __swap(lst, i, right)
                i = right

        # Only left node
        elif left < top:

            # If left node greater than parent swap
            if lst[left] <= lst[i]: break
            __swap(lst, i, left)
            i = left

        # Only right node
        elif right < top:

            # If right node greater than parent swap
            if lst[right] <= lst[i]: break
            __swap(lst, i, right)
            i = right

        else: break


def sort(lst: list):

    # Heapify
    for i in range((len(lst) - 2) // 2, -1 , -1):
        __siftDown(lst, i, len(lst))

    # Sort
    for i in range(len(lst) - 1, 0, -1):
        __swap(lst, i, 0)
        __siftDown(lst, 0, i)
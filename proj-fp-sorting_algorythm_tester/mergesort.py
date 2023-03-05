# Mergesort

def sort(lst: list):

    # Stop recursion
    if len(lst) <= 1: return

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Call recursively
    sort(left)
    sort(right)

    left_index = 0
    right_index = 0
    main_index = 0

    # Merge from left and right into main
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            lst[main_index] = left[left_index]
            left_index += 1
        else:
            lst[main_index] = right[right_index]
            right_index += 1
        main_index += 1

    # Merge remaining left only
    while left_index < len(left):
        lst[main_index] = left[left_index]
        left_index += 1
        main_index += 1

    # Merge remaining right only
    while right_index < len(right):
        lst[main_index] = right[right_index]
        right_index += 1
        main_index += 1

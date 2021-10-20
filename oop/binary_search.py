def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None.
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found")


some_list = sorted(["Apple", "blueberry", "Banana", "Strawberry", "peach", "Apricot"])
print(some_list)
result = binary_search(some_list, "apricot")
verify(result)

result = binary_search(some_list, "Apricot")
verify(result)
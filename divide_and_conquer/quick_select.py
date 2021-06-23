"""
Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. It is related to the quick sort sorting algorithm.

Example:
>> quick_select([6,4,5,1,3,2],3) -> 3
"""


def quick_select(arr: list[any], k: int) -> any:
    """
    Select the kth smallest element in an unordered list
    """
    if len(arr) == 0 or k > len(arr) or k == 0:
        raise RuntimeError("Invalid k")
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    smaller = []
    equal = []
    bigger = []
    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x > pivot:
            bigger.append(x)
        else:
            equal.append(x)
    if k <= len(smaller):
        return quick_select(smaller, k)
    if (k - len(smaller)) <= len(equal) and len(equal) > 0:
        return equal[0]
    else:
        return quick_select(bigger, k - len(smaller) - len(equal))


if __name__ == "__main__":
    print(quick_select([6, 4, 1, 3, 2, 5], 2))

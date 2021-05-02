"""
Stable quick sort: generate a new array, keep the order of original array
In place quick sort: mutate the order of original array
"""


def stable_quick_sort(arr: list[any]) -> list[any]:
    if (len(arr) <= 1):
        return arr
    pivot = arr[int((len(arr) - 1) / 2)]
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
    return stable_quick_sort(smaller) + equal + stable_quick_sort(bigger)


def in_place_quick_sort(arr: list) -> None:
    pass

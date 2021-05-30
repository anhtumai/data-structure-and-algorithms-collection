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

# Pseudo code for Partition
# Partition (A, left, right) [input = A[left .. right]]
# - pivot := A[left]
# - i := left + 1
# - for j = l + 1 to r
#       - if A[j] < p
#           - A[i], A[j] = A[j], A[i]
#           - i := i + 1
# - A[left], A[i-1] = A[i-1], A[left]


def in_place_quick_sort(arr: list) -> None:
    _partition(arr, 0, len(arr) - 1)


def _partition(arr: list, left: int, right: int) -> None:
    if left >= right:
        return
    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    _partition(arr, left, i - 2)
    _partition(arr, i, right)

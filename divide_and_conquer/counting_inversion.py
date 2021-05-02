"""
Problem:
Given an array L with n elements. Inversion occurs when L[i] > L[j] when 0 < i < j < n.
Example:
count_inversions([1,3,5,2,4,6]) ->
Explanation: 3 pairs of inversions (3,2), (5,3), (5,4)
"""


def count_inversions(elems: list[any]) -> int:
    # return the number of inversions in the array without mutating it
    return _count(elems)[1]


def _count(elems: list[any]) -> tuple[list[any], int]:
    if len(elems) > 1:
        middle = int(len(elems) / 2)
        sorted_left, count_left = _count(elems[:middle])
        sorted_right, count_right = _count(elems[middle:])
        sorted_arr, count_split = _merge_and_count_split(
            sorted_left, sorted_right)
        return sorted_arr, count_left + count_right + count_split
    else:
        return elems, 0


def _merge_and_count_split(L: list[any], R: list[any]) -> tuple[list[any], int]:
    count = 0
    sorted_arr = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            sorted_arr.append(L[i])
            i += 1
        else:
            sorted_arr.append(R[j])
            j += 1
            count += len(L) - i
    if i < len(L):
        sorted_arr += L[i:]
    if j < len(R):
        sorted_arr += R[j:]
    return (sorted_arr, count)

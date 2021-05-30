"""
Given a sorted array of number and a target, return the index containing that target.
If target does not exist in the array, return -1.
Tested with Leetcode: https://leetcode.com/problems/binary-search

>> binary_search([0, 5, 11, 12, 15], 12) -> 3
>> binary_search([2,3,5,6,11], 4) -> -1

>> recursive_binary_search([0, 5, 11, 12, 15], 12) -> 3
>> recursive_binary_search([2,3,5,6,11], 4) -> -1
"""


def recursive_binary_search(l: list[any], target: any) -> int:

    def _binary_search(xs: list[any], checkpoint):
        if (len(xs)) == 0:
            return -1
        if (len(xs)) == 1 and xs[0] != target:
            return -1
        middle = len(xs) // 2
        if (target < xs[middle]):
            return _binary_search(xs[:middle], checkpoint)
        elif (target > xs[middle]):
            return _binary_search(xs[middle:], checkpoint + middle)
        return checkpoint + middle

    return _binary_search(l, 0)


def binary_search(xs: list[any], target: any) -> int:
    left, right = 0, len(xs) - 1
    while left <= right:
        middle = (right + left) // 2
        if (target < xs[middle]):
            right = middle - 1
        elif (target > xs[middle]):
            left = middle + 1
        else:
            return middle
    return -1

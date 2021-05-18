"""
Give 2 sorted arrays and a number x, find the pair whose sum is closest to x
Example:
compute([1,4,5,7], [10,20,30,40], 32) -> (1,30)
"""

import math


def get_closest_pair(xs: list[int], ys: list[int], target: int) -> tuple[int, int]:
    i, j = 0, len(ys) - 1
    min_dist = math.inf
    n1, n2 = xs[0], ys[-1]
    while (i < len(xs) and j >= 0):
        _sum = xs[i] + ys[j]
        new_dist = abs(_sum - target)
        if new_dist < min_dist:
            n1, n2 = xs[i], ys[j]
            min_dist = new_dist
        if _sum < target:
            i += 1
        elif _sum > target:
            j -= 1
        else:
            return xs[i], ys[j]
    return n1, n2


print(get_closest_pair([1, 4, 5, 7], [10, 20, 30, 40], 28))

"""
Given array of distinct elements.
Find triplets in the array whose sum is zero.

find_triplets([0, -1, 2, -3, 1]) -> [(0,-1,1),(2,-3,1)]

Tested with Leetcode: https://leetcode.com/problems/3sum
"""


def find_triplets(nums: list[int]) -> list[int]:
    xs = sorted(nums)

    if len(xs) < 3:
        return []
    if len(xs) == 3:
        if (xs[0] + xs[1] + xs[2] == 0):
            return [xs]
        else:
            return []
    res = set()
    for i in range(len(xs) - 2):
        triplets = find_pair(xs[(i+1):], 0-xs[i])
        for triplet in triplets:
            res.add(triplet)
    return list(res)[::-1]


def find_pair(arr: list[int], _sum: int) -> tuple[int, int, int]:
    """Assume arr is sorted"""
    i, j = 0, len(arr) - 1
    res = []
    while i < j:
        new_sum = arr[i] + arr[j]
        if new_sum < _sum:
            i += 1
        elif new_sum > _sum:
            j -= 1
        else:
            res.append((0 - _sum, arr[i], arr[j]))
            i += 1
            j -= 1
    return res


print(find_triplets([-1, 0, 1, 2, -1, -4]))

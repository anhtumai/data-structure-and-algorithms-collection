"""
Find pair in an array that sum to a specific value
"""


def find_sum_pair(arr: list[int], _sum: int) -> tuple[int, int]:
    xs = sorted(arr)
    i, j = 0, len(xs) - 1
    while i < j:
        if xs[i] + xs[j] < _sum:
            i += 1
        elif xs[i] + xs[j] > _sum:
            j -= 1
        else:
            return xs[i], xs[j]
    return None, None


print(find_sum_pair([5, 1, 4, 6, 1, 4], 12))

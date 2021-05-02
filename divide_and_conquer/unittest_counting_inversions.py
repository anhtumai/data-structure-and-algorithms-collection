"""
Origin of sample test: Divide and Conquer, Sorting and Searching, and Randomized Algorithms course by Standford
"""

from counting_inversion import count_inversions


def parse_file(path: str) -> list[int]:
    res = []
    with open(path, "r") as f:
        for line in f:
            res.append(int(line))
    return res


if __name__ == "__main__":
    l = parse_file("sample_test_for_counting_inversions.txt")
    answer = count_inversions(l)
    assert(answer == 2407905288)

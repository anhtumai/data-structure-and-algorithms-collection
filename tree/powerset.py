"""
Given the list of item, generate all possible subsets of that
Example:

>> powerset([1,2,3])
>> [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

2 approaches:

Decision Tree + Recusion implementation

Bitwise Manipulation implementation
Explanation: https://www.youtube.com/watch?v=9oPNGofa1pI&t=97s

Supposed you have a list of [1,2,3] then the result will have 8=2^3 indices.
Let's look at bit reprenstation from 0 to 7:
0   000
1   001
2   010
...
6   110
7   111

Surprisingly, the bits can represent how we put items into the subset,
with '1': we take the item, with '0': we leave it.
'110' can represent [2,3] (with bitwise manipulation, the order is reversed,
so it is [2,3] instead of [1,2]), '010' can represent [2].

To get bit value (0 or 1) of number n at the index i (the last bit index is 0),
we shift n by i to the right and get the remainder when dividing it by 2: `bit = (n >> i) % 2`
"""

Item=any
Subset=list[any]

def recurs_powerset(items: list[Item]) -> list[Subset]:
    """Generate all subsets of a list"""
    res: list[Subset] = []

    def helper(subset: Subset, i: int) -> None:
        """Fill in powerset result while iterating through the list"""
        if i == len(items):
            res.append(subset)
        else:
            helper(subset, i + 1)
            helper(subset + [items[i]], i + 1)

    helper([], 0)
    return res


def bitwise_powerset(items: list[any]):
    """Generate all subsets of a list"""
    res: list[list[any]] = []
    N = len(items)

    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        subset = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                subset.append(items[j])
        res.append(subset)
    return res


if __name__ == "__main__":
    print(recurs_powerset([1, 2, 3]))
    print(bitwise_powerset([1, 2, 3]))

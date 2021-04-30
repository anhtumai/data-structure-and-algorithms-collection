def stable_quick_select(arr: list[any], k: int) -> any:
    if (len(arr) == 0 or k > len(arr) or k == 0):
        raise RuntimeError("Invalid k")
    if (len(arr) == 1):
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
        return stable_quick_select(smaller, k)
    if (k - len(smaller)) <= len(equal) and len(equal) > 0:
        return equal[0]
    else:
        return stable_quick_select(bigger, k - len(smaller) - len(equal))


if __name__ == "__main__":
    xs = [10, 9, 5, 2, 1, 5, 19, 3, 3, 3, 3, 3, 1, 4, 5, 2]
    for i in range(1, len(xs) + 1):
        print(stable_quick_select(xs, i))

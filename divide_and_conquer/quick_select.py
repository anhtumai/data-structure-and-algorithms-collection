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

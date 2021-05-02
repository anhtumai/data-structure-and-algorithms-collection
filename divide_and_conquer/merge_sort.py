def stable_merge_sort(elems: list[any]) -> list[any]:
    if len(elems) > 1:
        middle = int(len(elems) / 2)
        sorted_left = stable_merge_sort(elems[:middle])
        sorted_right = stable_merge_sort(elems[middle:])
        return stable_merge(sorted_left, sorted_right)
    else:
        return elems


def stable_merge(L: list[any], R: list[any]) -> list[any]:
    res = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    if i < len(L):
        res += L[i:]
    if j < len(R):
        res += R[j:]
    return res

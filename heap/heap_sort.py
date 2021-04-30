from typing import List, Any
from minmax_heap import MinHeap


def heapsort(elems: List[Any]) -> List[Any]:
    min_heap = MinHeap(elems)
    res = []
    while (len(res) < len(elems)):
        res.append(min_heap.poll())
    return res


if __name__ == "__main__":
    l = [10, 4, 5, 132, 13, 4, 1, 3, 0]
    print(heapsort(l))

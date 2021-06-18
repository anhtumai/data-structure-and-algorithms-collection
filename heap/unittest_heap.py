import unittest
from minmax_heap import MinHeap, MaxHeap


class Node(object):
    def __init__(self, name: str, distance: int):
        self.name = name
        self.distance = distance

    def __repr__(self):
        return f"({self.name},{self.distance})"

    def __lt__(self, other):
        return self.distance < other.distance


class TestHeap(unittest.TestCase):
    def test_min_heap(self):
        xs = [10, 3, 5, 2, 19, 13, 1]
        min_heap = MinHeap(xs)
        sorted_xs = sorted(xs)
        for x in sorted_xs: 
            self.assertEqual(x, min_heap.poll())

    def test_max_heap(self):
        xs = [10, 3, 5, 2, 19, 13, 1]
        max_heap = MaxHeap(xs)
        sorted_xs = sorted(xs)
        for x in sorted_xs[::-1]:
            self.assertEqual(x, max_heap.poll())

    def test_decrease_key(self):
        nodes = [Node("R", -1), Node("B", 6), Node("A", 3), Node("X", 1), Node("E", 4)]
        min_heap = MinHeap(nodes)
        min_heap.decrease_key("B", -17)
        root = min_heap.peek()
        self.assertEqual(root.name, "B")
        self.assertEqual(root.distance, -17)


if __name__ == "__main__":
    unittest.main()

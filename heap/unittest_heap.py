import unittest
from minmax_heap import MinHeap, MaxHeap


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

    def test_replace(self):
        xs = [4, 2, 5, 19, 42, 3, 1]
        min_heap = MinHeap(xs)
        print(str(min_heap))
        min_heap.replace(3, 0)
        print(str(min_heap))


if __name__ == "__main__":
    unittest.main()

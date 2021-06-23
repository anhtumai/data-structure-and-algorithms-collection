"""
Origin of sample test: Graph Search, Shortest Paths, and Data Structures course by Standford
"""

import unittest
from median_heap import MedianHeap, get_median


class TestMedianHeap(unittest.TestCase):
    def test_peek(self):
        xs = [4, 3, 6, 2, 9, 10, 40, 1, 2, 100]
        for i in range(1, len(xs) + 1):
            heap = MedianHeap(xs[:i])
            self.assertEqual(get_median(xs[:i]), heap.peek())

    def test_poll(self):
        xs = [4, 3, 6, 2, 9, 10, 40, 1, 5, 100, 5, 4, 5, 5, 5, 5, 5]
        heap = MedianHeap(xs)
        for i in range(len(xs)):
            median = get_median(xs)
            self.assertEqual(heap.poll(), median)
            xs.remove(median)
        self.assertRaises(RuntimeError, heap.poll)

    def test_add(self):
        xs = [4, 3, 6, 2, 9, 10, 40, 1, 5, 100, 5, 4, 5, 5, 5, 5, 5]
        heap = MedianHeap([])
        for i in range(len(xs)):
            heap.add(xs[i])
            self.assertEqual(heap.peek(), get_median(xs[: (i + 1)]))

    def test_with_file(self):
        median_heap = MedianHeap([])
        res = 0
        with open("Median.txt", "r") as f:
            for line in f:
                median_heap.add(int(line))
                res += median_heap.peek()
        self.assertEqual(res, 46831213)


if __name__ == "__main__":
    unittest.main()

"""
A MedianHeap is a special data structure designed specifically for this problem:
Generating a running median for a series of streaming numbers

A MedianHeap has exactly the same interface of Min, Max Heap, but when we pop a
MedianHeap, we get median value, not min or max value

Public functions:
- add(item: any) -> None: add new item to the heap
- peek() -> any: Return the root value, which is the median value of all elements in the heap
- poll() -> any: Remove and return the root value
"""

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from divide_and_conquer.quick_select import quick_select
from minmax_heap import MinHeap, MaxHeap


def get_median(elems: list[any]) -> any:
    """Return median value of an array"""
    return quick_select(elems, int((len(elems) - 1) / 2) + 1)


class MedianHeap:
    def __init__(self, elems: list[any]):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        if len(elems) > 0:
            median = get_median(elems)
        for elem in elems:
            if elem <= median:
                self.max_heap.add(elem)
            else:
                self.min_heap.add(elem)

    def add(self, item: any) -> None:
        if self.max_heap.size() == 0:
            self.max_heap.add(item)
            return
        max_smaller = self.max_heap.peek()
        if self.min_heap.size() == 0:
            if item < max_smaller:
                median_value = self.max_heap.poll()
                self.max_heap.add(item)
                self.min_heap.add(median_value)
            else:
                self.min_heap.add(item)
            return
        min_bigger = self.min_heap.peek()

        if max_smaller < item < min_bigger:
            if self.max_heap.size() <= self.min_heap.size():
                self.max_heap.add(item)
            else:
                self.min_heap.add(item)
        elif item <= max_smaller:
            self.max_heap.add(item)
            if self.max_heap.size() - self.min_heap.size() > 1:
                median_value = self.max_heap.poll()
                self.min_heap.add(median_value)
        else:
            self.min_heap.add(item)
            if self.max_heap.size() < self.min_heap.size():
                median_value = self.min_heap.poll()
                self.max_heap.add(median_value)

    def peek(self) -> any:
        if self.max_heap.size() >= self.min_heap.size():
            return self.max_heap.peek()
        else:
            return self.min_heap.peek()

    def poll(self) -> any:
        if self.max_heap.size() >= self.min_heap.size():
            return self.max_heap.poll()
        else:
            return self.min_heap.poll()

    def __str__(self):
        return "(" + str(self.max_heap) + "-" + str(self.min_heap) + ")"

import os
import sys
from minmax_heap import MinHeap, MaxHeap

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from divide_and_conquer.quick_select import stable_quick_select

def get_median(elems: list[any]) -> any:
    return stable_quick_select(elems, int((len(elems) - 1) / 2) + 1)


class MedianHeap:
    def __init__(self, elems: list[any] = []):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        if len(elems) > 0:
            median = get_median(elems)
        for elem in elems:
            if (elem <= median):
                self.max_heap.add(elem)
            else:
                self.min_heap.add(elem)

    def add(self, item: any) -> None:
        if(self.max_heap.size() == 0):
            self.max_heap.add(item)
            return
        else:
            max_smaller = self.max_heap.peek()
        if(self.min_heap.size() == 0):
            if (item < max_smaller):
                x = self.max_heap.poll()
                self.max_heap.add(item)
                self.min_heap.add(x)
            else:
                self.min_heap.add(item)
            return
        min_bigger = self.min_heap.peek()

        if (max_smaller < item < min_bigger):
            if self.max_heap.size() <= self.min_heap.size():
                self.max_heap.add(item)
            else:
                self.min_heap.add(item)
        elif item <= max_smaller:
            self.max_heap.add(item)
            if (self.max_heap.size() - self.min_heap.size() > 1):
                x = self.max_heap.poll()
                self.min_heap.add(x)
        else:
            self.min_heap.add(item)
            if (self.max_heap.size() < self.min_heap.size()):
                x = self.min_heap.poll()
                self.max_heap.add(x)

    def peek(self) -> any:
        if (self.max_heap.size() >= self.min_heap.size()):
            return self.max_heap.peek()
        else:
            return self.min_heap.peek()

    def poll(self) -> any:
        if (self.max_heap.size() >= self.min_heap.size()):
            return self.max_heap.poll()
        else:
            return self.min_heap.poll()

    def __str__(self):
        return "(" + str(self.max_heap) + "-" + str(self.min_heap) + ")"

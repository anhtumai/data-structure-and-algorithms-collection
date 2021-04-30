import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(parentdir)
sys.path.append(rootdir + "/heap")

from median_heap import MedianHeap

if __name__ == "__main__":
    median_heap = MedianHeap()
    res = 0
    with open("Median.txt", "r") as f:
        for line in f:
            median_heap.add(int(line))
            res += median_heap.peek()
    assert(res == 46831213)
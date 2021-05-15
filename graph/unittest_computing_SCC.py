"""
Origin of sample test: Graph Search, Shortest Paths, and Data Structures course by Standford
"""

from compute_strong_components import compute_scc

import resource
import sys
import unittest

# Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


def load_graph(path):
    graph = {}

    with open(path, "r") as reader:
        lines = reader.readlines()
        for line in lines:
            a = line.split(" ")
            if int(a[0]) == int(a[1]):
                continue
            if int(a[0]) in graph:
                graph[int(a[0])].append(int(a[1]))
            else:
                graph[int(a[0])] = [int(a[1])]
    return graph


class TestComputingSCC(unittest.TestCase):
    def test(self):
        graph = load_graph("sample_test_for_computing_SCC.txt")
        res = compute_scc(graph)
        self.assertEqual(sorted(res)[-5:], [211, 313, 459, 968, 434821])


if __name__ == "__main__":
    unittest.main()

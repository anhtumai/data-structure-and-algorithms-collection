"""
Origin of sample test: Graph Search, Shortest Paths, and Data Structures course by Standford
"""

import unittest
from Djisktra_search_with_heap import get_distances_and_parents


def parse_input(path):
    graph = {}

    with open(path, "r") as reader:
        lines = reader.readlines()
        for line in lines:
            a = line.split()
            graph[int(a[0])] = list(
                map(lambda s: (int(s.split(',')[0]), int(
                    s.split(',')[1])), a[1:]))

    return graph


class TestCase(unittest.TestCase):
    def test(self):
        graph = parse_input("sample_test_for_Djikstra.txt")
        distances, froms = get_distances_and_parents(graph, 1)

        vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        calculated_distances = list(
            map(lambda vertex: distances[vertex], vertices))
        self.assertEqual(calculated_distances, [
                         2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068])


if __name__ == "__main__":
    unittest.main()

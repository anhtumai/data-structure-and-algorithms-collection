"""
Djisktra Shortest Path algorithm
Given a graph which is represented by adjacent lists, starting node and destination node.
For example:
graph = {"A": [("B", 12), ("C", 5)]} means there exists a path A -> B with length 12, A-> C with length 5.

Return: a list, representing the path from stating to destination node
"""
import math

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from heap.minmax_heap import MinHeap

Graph = dict[any, list[tuple[any, int]]]
Distancedict = dict[any, int]
Parentdict = dict[any, any]


class Node(object):
    def __init__(self, name: str, distance: int):
        self.name = name
        self.distance = distance

    def __repr__(self):
        return f"({self.name},{self.distance})"

    def __lt__(self, other):
        return self.distance < other.distance


def initialize(graph: Graph, start: any) -> tuple[Distancedict, Parentdict, MinHeap]:
    """Initialize variables before performing Djisktra algorithms
    Input:
        graph: adjacent list representation of a graph
        start: name of starting point
    Returns:
        distances: a key-value pair of name of node and its minimum distance from start
        parents: a key-value pair of name of a node and its parent
        min_heap: a MinHeap to get node with minimum distance in O(log(n)) time.
    """
    node_names = set()
    for key in graph:
        node_names.add(key)
        for value in graph[key]:
            node_names.add(value[0])
    distances = {node_name: math.inf for node_name in node_names}
    parents = {node_name: None for node_name in node_names}
    min_heap = MinHeap(
        [
            Node(node_name, distances[node_name])
            for node_name in node_names
            if node_name != start
        ]
    )
    min_heap.add(Node(start, 0))
    distances[start] = 0
    parents[start] = start
    return (distances, parents, min_heap)


def get_distances_and_parents(
    graph: Graph, start: any
) -> tuple[Distancedict, Parentdict]:
    """Find the shorted path from starting point to other nodes in the graph, return their minimum distances and parents
    Input:
        graph: adjacent list representation of a graph
        start: name of starting point
    Returns:
        distances: a key-value pair of name of node and its minimum distance from start
        parents: a key-value pair of name of a node and its parent
    """
    # Initialize
    distances, parents, min_heap = initialize(graph, start)

    # Compute
    while not min_heap.is_empty():
        node = min_heap.poll()
        s = node.name
        for (adj_name, ajd_distance) in graph[s]:
            new_distance = ajd_distance + distances[s]
            if distances[adj_name] > new_distance:
                distances[adj_name] = new_distance
                min_heap.replace_with_condition(
                    lambda node: node.name == adj_name, Node(adj_name, new_distance)
                )
                parents[adj_name] = s
    return (distances, parents)


def get_path(parents: Parentdict, start: any, end: any) -> list[any]:
    """Return a list of nodes from start node to end node given a key-pair value of node and its parent"""
    path: list[any] = [end]
    while end != start:
        path.append(parents[end])
        end = parents[end]
    path.reverse()
    return path


def djisktra(graph: Graph, start: any, end: any) -> list[any]:
    """Return shortest path from start to end"""
    _, parents = get_distances_and_parents(graph, start)
    return get_path(parents, start, end)


if __name__ == "__main__":
    # Example source:
    # https://www.codingame.com/playgrounds/1608/shortest-paths-with-dijkstras-algorithm/dijkstras-algorithm
    sample_graph = {
        "A": [("B", 3), ("C", 1)],
        "B": [("D", 5), ("C", 7), ("A", 3), ("E", 1)],
        "C": [("A", 1), ("B", 7)],
        "D": [("B", 5), ("E", 7)],
        "E": [("D", 7), ("B", 1)],
    }
    path = djisktra(sample_graph, "A", "E")
    print(path)  # ['A', 'B', 'E']

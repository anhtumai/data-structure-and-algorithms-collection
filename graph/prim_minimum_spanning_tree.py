"""
Minimum Spanning Tree of graph G: subset of edges of G that farm a tree
and hit all vertices of G (without forming a cycle). 

Prim's algorithm
- initially a min heap storing all nodes in graph G 
    - start.distance = 0 for arbitrary start vertex in G
    - for v in G-{start}, v.distance = infinity
- while MinHeap is not empty:
    - u = MinHeap (=> add u to ParentDict)
    - for neighbour v in adjacent[u]:
        - if v is in MinHeap (which means v is not in ParentDict) and edge(u, v) < distances[v]:
            distances[v] = edge(u, v)
            parents[v] = u
- return a ParentDict

"""

from typing import Union

import math

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from heap.minmax_heap import MinHeap

NodeName = Union[str, int]
Graph = dict[NodeName, list[tuple[NodeName, int]]]
DistanceDict = dict[NodeName, int]
ParentDict = dict[NodeName, NodeName]


class Node:
    """
    Representing a vertex in a graph with its minimum distance from subset S.
    """

    def __init__(self, name: str, distance: int):
        self.name = name
        self.distance = distance

    def __repr__(self):
        return f"({self.name},{self.distance})"

    def __lt__(self, other):
        return self.distance < other.distance


def initialize(graph: Graph, start: any) -> tuple[DistanceDict, ParentDict, MinHeap]:
    """Initialize variables before performing Prim's algorithm
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


def prim_mst_get_parents(graph: Graph, start: NodeName) -> ParentDict:
    """Find the path going through all nodes of a graph with minimum weight
    using Prim's greedy algorithm
    Input:
        graph: adjacent list representation of a graph
        start: name of starting point
    Return:
        parents: a key-value pair of name of a node and its parent
    """
    distances, parents, min_heap = initialize(graph, start)
    explored = set()
    while not min_heap.is_empty():
        node = min_heap.poll()
        s = node.name
        explored.add(s)
        for (adj_name, adj_distance) in graph[s]:
            if adj_name not in explored and adj_distance < distances[adj_name]:
                distances[adj_name] = adj_distance
                min_heap.decrease_key(adj_name, distances[adj_name])
                parents[adj_name] = s

    return parents


if __name__ == "__main__":
    graph1 = {
        "1": [("6", 10), ("2", 28)],
        "2": [("1", 28), ("3", 16), ("7", 14)],
        "3": [("2", 16), ("4", 12)],
        "4": [("3", 12), ("5", 22), ("7", 18)],
        "5": [("4", 22), ("6", 25), ("7", 24)],
        "6": [("1", 10), ("5", 25)],
        "7": [("5", 24), ("2", 14), ("4", 18)],
    }

    print(prim_mst_get_parents(graph1, "1"))

    graph2 = {
        "A": [("B", 7), ("C", 8)],
        "B": [("A", 7), ("C", 3)],
        "C": [("B", 3), ("A", 8), ("D", 4), ("E", 3)],
        "D": [("B", 6), ("C", 4), ("E", 2), ("F", 5)],
        "E": [("D", 2), ("C", 3), ("F", 2)],
        "F": [("D", 5), ("E", 2)],
    }
    print(prim_mst_get_parents(graph2, "A"))

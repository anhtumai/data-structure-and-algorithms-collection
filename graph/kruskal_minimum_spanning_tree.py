"""
Kruskal minimum spanning tree

This algorithm is based on a fact: the global minimum-weight edge must be
the element of minimum spanning tree.

Kruskal algorithm:
- Initialize a disjoint set with all nodes from graph
- Sort all edges by weight
- for edge in sorted edges:
    - if Find-Set(edge.u) != Find-Set(edge.v):
        - add this edge into minimum spanning tree
        - Union-Sets(edge.u, edge.v)
"""

from dataclasses import dataclass
from typing import Union

from disjoint_set import DisjointSet


Vertex = Union[str, int]
Graph = dict[Vertex, list[tuple[Vertex]]]


@dataclass(frozen=True)
class Edge:
    """Representing edge in graph"""
    u: Vertex
    v: Vertex
    weight: int


def get_all_nodes(graph: Graph) -> list[Vertex]:
    """
    Return a list of all nodes in the graph
    """
    mentioned_nodes = set()
    for node in graph.keys():
        mentioned_nodes.add(node)
        for neighbour, _ in graph[node]:
            mentioned_nodes.add(neighbour)
    return list(mentioned_nodes)


def get_all_edges(graph: Graph) -> list[Edge]:
    """
    Return a list of all edges in the undirected graph
    Note: edge will not be dupplicated
    """
    mentioned_nodes = set()
    res: list[Edge] = []
    for node in graph.keys():
        for (destination, weight) in graph[node]:
            if destination not in mentioned_nodes:
                res.append(Edge(node, destination, weight))
        mentioned_nodes.add(node)
    return res


def kruskal_minimum_spanning_tree(graph: Graph) -> list[Edge]:
    """Return list of edges, representing minimum spanning tree"""
    vertices = get_all_nodes(graph)
    edges = get_all_edges(graph)

    djs = DisjointSet(vertices)
    sorted_edges = sorted(edges, key=lambda edge: edge.weight)

    res: list[Edge] = []
    for edge in sorted_edges:
        if djs.find_set(edge.u) != djs.find_set(edge.v):
            res.append(edge)
            djs.union_sets(edge.u, edge.v)
    return res


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
    print(kruskal_minimum_spanning_tree(graph1))

    graph2 = {
        "A": [("B", 7), ("C", 8)],
        "B": [("A", 7), ("C", 3)],
        "C": [("B", 3), ("A", 8), ("D", 4), ("E", 3)],
        "D": [("B", 6), ("C", 4), ("E", 2), ("F", 5)],
        "E": [("D", 2), ("C", 3), ("F", 2)],
        "F": [("D", 5), ("E", 2)],
    }
    print(kruskal_minimum_spanning_tree(graph2))

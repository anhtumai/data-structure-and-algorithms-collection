"""
Compute Strongly Connected Components

Given a graph, calculate number of strongest connected components

In a subgraph, if we can reach from every vertex to every other vertex,
then it is called SCC.

Example:
>> graph1 = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5, 7], 5: [6], 6: [4, 7]}                                                                                         >>> compute_sccs(graph1))
>> [[0, 2, 1], [3], [4, 6, 5], [7]] 


Approach: Using Kosaraju Algorithm:

- Perform DFS traversal of a graph,
to get a stack representing the order of visited nodes while traversal.
(The starting node will be returned when we pop the stack for the first time)
- Perform DFS traversal of a reversed graph, where directions of all edges are reversed
- Collect strongly connected components while traversal

Tested with: https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/tutorial/

"""

from typing import Generator

Node = any
Graph = dict[Node, list[Node]]
Stack = list[Node]


def genrate_all_nodes(graph: Graph) -> Generator[int, None, None]:
    """
    Return a generator for all nodes in the graph
    """
    mentioned_nodes = set()
    for node in graph.keys():
        if node not in mentioned_nodes:
            yield node
            mentioned_nodes.add(node)
            for neighbour in graph[node]:
                if neighbour not in mentioned_nodes:
                    yield neighbour
                    mentioned_nodes.add(neighbour)


def reverse(graph: Graph) -> Graph:
    """
    Return a new graph with same vertices as input graph, but all edges are reversed
    """
    reverse_graph = {}

    for node in graph.keys():
        for neighbour in graph[node]:
            if neighbour not in reverse_graph:
                reverse_graph[neighbour] = [node]
            else:
                reverse_graph[neighbour].append(node)
    return reverse_graph


def get_dfs_stack(graph: Graph) -> Stack:
    """
    Perform DFS traversal in an input graph
    Return a stack, representing the order of the path
    (the starting node will be returned when we pop the stack for the first time)
    """
    explored = set()
    stack = []

    def dfs_util(node: Node) -> None:
        explored.add(node)
        if node in graph:
            for neighbour in graph[node]:
                if neighbour not in explored:
                    dfs_util(neighbour)
        stack.append(node)

    for node in genrate_all_nodes(graph):
        if node not in explored:
            dfs_util(node)

    return stack


def get_strongly_connected_components(graph: Graph, stack: Stack) -> list[list[Node]]:
    """
    Perfrom DFS traversal on a reversed graph to get
    """
    explored = set()
    sccs = []

    def dfs_util(node: Node, scc: list[Node]) -> list[Node]:
        explored.add(node)
        scc.append(node)
        if node in graph:
            for neighbour in graph[node]:
                if neighbour not in explored:
                    dfs_util(neighbour, scc)
        return scc

    while len(stack) > 0:
        node = stack.pop()
        if node not in explored:
            sccs.append(dfs_util(node, []))
    return sccs


def compute_sccs(graph: Graph) -> list[list[Node]]:
    """
    Given a directed graph, return the list of strongly connected components
    """
    reverse_graph = reverse(graph)
    stack = get_dfs_stack(graph)
    sccs = get_strongly_connected_components(reverse_graph, stack)
    return sccs


if __name__ == "__main__":
    graph1 = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5, 7], 5: [6], 6: [4, 7]}
    print(compute_sccs(graph1))  # [[0, 2, 1], [3], [4, 6, 5], [7]]

    graph2 = {
        1: [10],
        3: [6, 9],
        7: [12],
        9: [2, 14],
        12: [9],
        4: [11],
        2: [5, 10],
        5: [3],
        15: [3, 8],
        8: [11],
        11: [5],
    }
    print(compute_sccs(graph2))
    # [[15], [8], [4], [11], [7], [12], [3, 5, 2, 9], [14], [6], [1], [10]]

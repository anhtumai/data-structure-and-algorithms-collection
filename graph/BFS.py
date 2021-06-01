"""
Breadth First Search
Given a graph which is represented by adjacent lists, starting node and destination node
For example:
graph = { "A" : ["B", "C"], "B": ["D"] } means there exists a path A -> B, A -> C and B -> D

Assume all paths have same length.

Return: a list, representing the shortest path from starting to destionation node

Example: bfs({ "A" : ["B", "C"], "B": ["D"] }, "A", "D") -> ["A", "B", "D"]

"""

from queue import Queue

Node = any
Graph = dict[Node, list[Node]]
ParentDict = dict[Node, Node]


def get_parents(graph: Graph, start: Node) -> ParentDict:
    """Return a key-value pair of a node and its parent
    when traversing down a path from a start node

    >> get_parents({ "A": ["B", "C"], "B": ["D"] }, "A") -> {"B": "A", "C": "A", "D": "B"}
    """

    queue = Queue()
    parents: ParentDict = {}
    explored: set[Node] = set()

    explored.add(start)
    queue.put(start)

    while not queue.empty():
        new_node: Node = queue.get()
        if new_node not in graph:
            continue
        for neighbour in graph[new_node]:
            if neighbour not in explored:
                explored.add(neighbour)
                parents[neighbour] = new_node
                queue.put(neighbour)

    return parents


def get_path(parent: ParentDict, start: Node, end: Node) -> list[Node]:
    """Get shortest path from start to end node from the parent dict
    """
    path = [end]
    while end != start:
        path.append(parent[end])
        end = parent[end]
    path.reverse()
    return path


def bfs(graph: Graph, start: Node, end: Node) -> list[Node]:
    """Get shortest path from start to end node from a graph
    """
    parents = get_parents(graph, start)
    if end in parents:
        path = get_path(parents, start, end)
        return path
    return []


if __name__ == "__main__":
    sample_graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["B", "F"],
        "E": ["F"]
    }

    shortest_path: list[Node] = bfs(sample_graph, "A", "F")
    print(shortest_path)  # ["A", "C", "F"]

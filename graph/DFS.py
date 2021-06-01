"""
Depth First Search
Given a graph which is represented by adjacent lists, starting node and destination node
For example:
graph = { "A" : ["B", "C"], "B": ["D"] } means there exists a path A -> B, A -> C and B -> D

Assume all paths have same length.

Return: a list, representing the path (may not be shortest) from starting to destionation node

Example: dfs({ "A" : ["B", "C"], "B": ["D"] }, "A", "D") -> ["A", "B", "D"]

"""


Node = any
Graph = dict[Node, list[Node]]
ParentDict = dict[Node, Node]


def get_parents(graph: dict[str, list[str]], start: str) -> dict[str, str]:
    """Return a key-value pair of a node and its parent
    when traversing down a path from a start node"""

    explored: set[Node] = set()
    parents: ParentDict = {}

    def dfs_util(new_node: Node) -> None:
        """Update parents dict while traversing the graph in depth"""
        explored.add(new_node)
        if new_node not in graph:
            return
        for neighbour in graph[new_node]:
            if neighbour not in explored:
                parents[neighbour] = new_node
                dfs_util(neighbour)

    dfs_util(start)
    return parents


def get_path(parents: ParentDict, start: Node, end: Node) -> list[Node]:
    """Return a list of nodes from start node to end node
    given a key-pair value of node and its parents"""
    path: list[str] = [end]
    while end != start:
        path.append(parents[end])
        end = parents[end]
    path.reverse()
    return path


def dfs(graph: dict[str, list[str]], start: str, end: str):
    """Return a list of nodes from start to end node given a graph"""
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

    shortest_path: list[Node] = dfs(sample_graph, "A", "F")
    print(shortest_path)  # ['A', 'B', 'E', 'F']

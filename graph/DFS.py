graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def get_parents(graph: dict[str, list[str]], start: str) -> dict[str, str]:
    """Return a key-value pair of a node and its parent when traversing down a path from a start node"""
    explored = set()
    parents: dict[str, str] = {}

    def dfs_util(s: str) -> None:
        explored.add(s)
        for w in graph[s]:
            if w not in explored:
                parents[w] = s
                dfs_util(w)
    dfs_util(start)
    return parents


def get_path(parents: dict[str, str], start: str, end: str) -> list[str]:
    """Return a list of nodes from start node to end node given a key-pair value of node and its parents"""
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
    else:
        return []


a = dfs(graph, "A", "F")
print(a)

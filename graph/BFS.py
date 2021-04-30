from queue import Queue

Graph = dict[any, list[any]]
ParentDict = dict[any, any]

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def get_traverse_path(graph: Graph, s: any) -> ParentDict:

    queue = Queue()
    parent = {}
    explored = set()

    explored.add(s)
    queue.put(s)

    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                parent[w] = v
                queue.put(w)

    return parent


def get_path(parent: ParentDict, start: any, end: any) -> list[any]:
    path = [end]
    while end != start:
        path.append(parent[end])
        end = parent[end]
    path.reverse()
    return path


def bfs(graph: Graph, start: any, end: any) -> list[any]:
    parents = get_traverse_path(graph, start)
    if end in parents:
        path = get_path(parents, start, end)
        return path
    else:
        return []


a = bfs(graph, "A", "F")
print(a)

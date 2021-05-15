def get_size(graph):
    size = 0
    for i in graph:
        if i > size:
            size = i
        for j in graph[i]:
            if j > size:
                size = j
    return size


def reverse(graph):
    reverse_graph = {}

    for key in graph.keys():
        for item in graph[key]:
            if item not in reverse_graph.keys():
                reverse_graph[item] = [key]
            else:
                reverse_graph[item].append(key)
    return reverse_graph


def dfs_loop(graph, size):
    explored = set()
    t = 0

    def dfs(graph, i):
        explored.add(i)

        if (i in graph):
            for j in graph[i]:
                if (j not in explored):
                    dfs(graph, j)
        nonlocal t
        t += 1
        f[i-1] = t

    f = [0 for i in range(size)]
    for i in range(size, 0, -1):
        if (i not in explored):
            dfs(graph, i)

    return f


def upgrade_with_fin_time(graph, f):
    new_graph = {}
    for i in graph:
        new_graph[f[i-1]] = list(map(lambda x: f[x-1], graph[i]))
    return new_graph


def dfs(graph, size):
    explored = set()
    res = []
    scc_size = 0

    def dfs_util(s):
        explored.add(s)
        nonlocal scc_size
        scc_size += 1
        if (s in graph):
            for j in graph[s]:
                if (j not in explored):
                    dfs_util(j)

    for i in range(size, 0, -1):
        if (i not in explored):
            explored.add(i)
            dfs_util(i)
            res.append(scc_size)
            scc_size = 0
    return res


def compute_scc(graph):
    size = get_size(graph)
    f = dfs_loop(reverse(graph), size)
    new_graph = upgrade_with_fin_time(graph, f)
    res = dfs(new_graph, size)
    return res

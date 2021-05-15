import random

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

# shuffle a graph order
keys = list(graph.keys())
random.shuffle(keys)
graph = dict([(key, graph[key]) for key in keys])


def topsort(graph):

    explored = set()
    stack = []

    def topsort_util(s):
        if s in explored:
            return
        explored.add(s)
        for w in graph[s]:
            if w not in explored:
                topsort_util(w)
        stack.append(s)

    for s in graph.keys():
        topsort_util(s)

    stack.reverse()
    return stack


order = topsort(graph)
print(order)

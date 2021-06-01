"""
Topological Sort

Given a DAG (Directed Acyclic Graph).
Acyclic graph is a graph doesn't have any cycle

Return a topological ordering, an ordering of the nodes where for each directed
edge from node A to node B, node A appears before node B in the ordering.

(The order may not be unique)

>> topsort({ "A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"] })
>> ["A", "B", "C", "D", "E"] or ["A", "C", "B", "D", "E"]

Motivation: Many real world situations can be modelled as a graph with directed edges
where some events must occur before others. For exp:
- School class preresquisities
- Program dependencies
- Event scheduling
"""

Node = any
Graph = dict[Node, list[Node]]


def topsort(graph: Graph) -> list[Node]:
    """Return a topological ordering from a directed acyclic graph
    """

    explored: set[Node] = set()
    stack = []

    def topsort_util(new_node: Node) -> None:
        """Update the stack while traversing the graph in depth
        """

        if new_node in explored:
            return
        explored.add(new_node)
        if new_node in graph:
            for neighbour in graph[new_node]:
                if neighbour not in explored:
                    topsort_util(neighbour)
        stack.append(new_node)

    for node in graph.keys():
        topsort_util(node)

    stack.reverse()
    return stack


if __name__ == "__main__":
    sample_graph_1 = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"]
    }

    order_1 = topsort(sample_graph_1)
    print(order_1)  # ['A', 'C', 'B', 'D', 'E']

    sample_graph_2 = {
        0: [2, 3, 6],
        1: [4],
        2: [6],
        3: [1, 4],
        4: [5, 8],
        6: [7, 11],
        7: [4, 12],
        9: [2, 10],
        10: [6],
        11: [12],
        12: [8]
    }

    order_2 = topsort(sample_graph_2)
    print(order_2)  # [9, 10, 0, 3, 1, 2, 6, 11, 7, 12, 4, 8, 5]

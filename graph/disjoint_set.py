"""
Disjoint set: an ADT 

Public functions:

- make_set(v): creates a new set consisting of the new element v
- union_sets(a,b): merges 2 specified sets (the set in which the element a
is located, and the set in which the element b is located)
- find_set(v): returns the representative of the set that contains the element v.
"""

from typing import Union

Vertex = Union[str, int]


class DisjointSet:
    def __init__(self, vertices: list[Vertex]):
        self.parents: dict[Vertex, Vertex] = {vertex: vertex for vertex in vertices}

    def union_sets(self, a: Vertex, b: Vertex) -> None:
        parent_a = self.parents[a]
        parent_b = self.parents[b]
        shared_parents = min(parent_a, parent_b)
        for v in self.parents.keys():
            if self.parents[v] in [parent_a, parent_b]:
                self.parents[v] = shared_parents

    def find_set(self, a: Vertex) -> Vertex:
        return self.parents[a]


if __name__ == "__main__":
    djs = DisjointSet([1, 2, 3, 4, 5, 6, 7])
    djs.union_sets(1, 5)
    print(djs.parents)
    print(djs.find_set(5))
    djs.union_sets(6, 1)
    djs.union_sets(5, 7)
    print(djs.parents)

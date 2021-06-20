"""
Disjoint set: an ADT 

Public functions:

- make_set(v): creates a new set consisting of the new element v
- union_sets(a,b): merges 2 specified sets (the set in which the element a
is located, and the set in which the element b is located)
- find_set(v): returns the representative of the set that contains the element v.

Implementation:
- DisjointSet is built with an underlying HashMap: parents
parents contain key-pair value of a vertex and its parent.
If some vertices share the same parent, they belong to the same set.
- To union 2 sets, I will choose the minimum of 2 sets' parents as a new shared parent.
Later, I change parents of all members of 2 sets to that value.
"""

from typing import Union

Vertex = Union[str, int]


class DisjointSet:
    def __init__(self, vertices: list[Vertex]):
        self.parents: dict[Vertex, Vertex] = {vertex: vertex for vertex in vertices}

    def union_sets(self, a: Vertex, b: Vertex) -> None:
        """
        Union set containing vertex a and set containing vertex b.
        Set parents of all members in 2 sets to a new shared parent.
        """
        parent_a = self.parents[a]
        parent_b = self.parents[b]
        shared_parents = min(parent_a, parent_b)
        for vertex in self.parents.keys():
            if self.parents[vertex] in [parent_a, parent_b]:
                self.parents[vertex] = shared_parents

    def find_set(self, vertex: Vertex) -> Vertex:
        """Return the parent of a vertex"""
        return self.parents[vertex]


if __name__ == "__main__":
    djs = DisjointSet([1, 2, 3, 4, 5, 6, 7])
    djs.union_sets(1, 5)
    print(djs.parents)
    print(djs.find_set(5))
    djs.union_sets(6, 1)
    djs.union_sets(5, 7)
    print(djs.parents)

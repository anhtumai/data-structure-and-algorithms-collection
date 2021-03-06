"""
Heap is a binary tree-based data structure, can be implemented using a list.
There are 2 types of heaps:
- Max-Heap: The key representing the root must be greatest among the keys which present
at all of its children. The same rule applies for all the subtrees.
- Min-Heap: The key representing the root must be smallest among the keys which present
at all of its children. The same rule applies for all the subtrees.

Heap Public method:
- size() -> int: return the number of elements
- is_empty() -> bool: check if the heap is empty
- peek() -> any: return the root value of the heap
- poll() -> any: remove and return the root value of the heap.
                 The heap perform self-tuning after removal
- add() -> None: add new element to the heap

For Min Heap only:
- decrease_key(name: any, new_distance: Union[int | float]) -> None: 
                 Find the node with the given name, update its distance to
                 lesser value (new_distance)
                 ( This function is created specifically for graph finding algorithms,
                 since we need to update the weight of a path when we find the shorter path.
                 This function assumes that Node datatype has 'name' and 'distance' property)
"""
from typing import Union


class Heap:
    def __init__(self, elems: list[any] = []):
        self.elems: list[any] = []
        for elem in elems:
            self.add(elem)

    def _has_left(self, index: int) -> bool:
        return index * 2 + 1 < len(self.elems)

    def _has_right(self, index: int) -> bool:
        return index * 2 + 2 < len(self.elems)

    def _has_parent(self, index: int) -> bool:
        return index != 0

    def _get_parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def _get_left_index(self, index: int) -> int:
        return index * 2 + 1

    def _get_right_index(self, index: int) -> int:
        return index * 2 + 2

    def _get_value(self, index: int) -> any:
        return self.elems[index]

    def _get_left(self, index: int) -> any:
        return self._get_value(self._get_left_index(index))

    def _get_right(self, index: int) -> any:
        return self._get_value(self._get_right_index(index))

    def _get_parent(self, index: int) -> any:
        return self._get_value(self._get_parent_index(index))

    def _heapify_up(self, start: int) -> None:
        raise NotImplementedError

    def _heapify_down(self, start: int = 0) -> None:
        raise NotImplementedError

    def size(self) -> int:
        return len(self.elems)

    def is_empty(self):
        return len(self.elems) == 0

    def peek(self) -> any:
        """Return the root element of the heap"""
        if len(self.elems) == 0:
            raise RuntimeError("Heap is empty")
        return self.elems[0]

    def poll(self) -> any:
        """Return and remove the current root element in the min heap"""
        if len(self.elems) == 0:
            raise RuntimeError("Heap is empty")
        res = self.elems[0]
        self.elems[0] = self.elems[-1]
        del self.elems[-1]
        self._heapify_down()
        return res

    def add(self, item) -> None:
        """Add new element to the heap and perform self-tuning"""
        self.elems.append(item)
        self._heapify_up(len(self.elems) - 1)

    def __str__(self):
        return str(self.elems)


class MinHeap(Heap):
    def _heapify_up(self, start: int) -> None:
        index = start
        while (
            self._has_parent(index)
            and self._get_value(self._get_parent_index(index)) > self.elems[index]
        ):
            parent_index = self._get_parent_index(index)
            self.elems[parent_index], self.elems[index] = (
                self.elems[index],
                self.elems[parent_index],
            )
            index = self._get_parent_index(index)

    def _heapify_down(self, start: int = 0) -> None:
        index = start
        while self._has_left(index):
            smaller_child_index = self._get_left_index(index)
            if self._has_right(index) and self._get_right(index) < self._get_left(
                index
            ):
                smaller_child_index = self._get_right_index(index)

            if self.elems[index] < self.elems[smaller_child_index]:
                return
            self.elems[index], self.elems[smaller_child_index] = (
                self.elems[smaller_child_index],
                self.elems[index],
            )
            index = smaller_child_index

    def decrease_key(self, name: any, new_distance: Union[int, float]) -> None:
        """Find the node with the given name, decrease its distance to new_distance.

        Args:
             name: name of replaced node
             new_distance: new distance of updated node
        Assumptions:
             Elements in heap tree must have name and distance property

        """
        for i in range(len(self.elems)):
            if self.elems[i].name == name:
                assert (
                    new_distance < self.elems[i].distance
                ), "new distance should be lesser than current distance"
                self.elems[i].distance = new_distance
                self._heapify_up(i)
                return


class MaxHeap(Heap):
    def _heapify_up(self, start: int) -> None:
        index = start
        while (
            self._has_parent(index)
            and self._get_value(self._get_parent_index(index)) < self.elems[index]
        ):
            parent_index = self._get_parent_index(index)
            self.elems[parent_index], self.elems[index] = (
                self.elems[index],
                self.elems[parent_index],
            )
            index = self._get_parent_index(index)

    def _heapify_down(self, start: int = 0) -> None:
        index = start
        while self._has_left(index):
            bigger_child_index = self._get_left_index(index)
            if self._has_right(index) and self._get_right(index) > self._get_left(
                index
            ):
                bigger_child_index = self._get_right_index(index)

            if self.elems[index] > self.elems[bigger_child_index]:
                return
            self.elems[index], self.elems[bigger_child_index] = (
                self.elems[bigger_child_index],
                self.elems[index],
            )
            index = bigger_child_index

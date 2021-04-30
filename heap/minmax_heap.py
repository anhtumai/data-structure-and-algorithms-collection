from typing import Callable


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

    def peek(self):
        """Return the smallest element"""
        if (len(self.elems) == 0):
            raise RuntimeError("Heap is empty")
        return self.elems[0]

    def poll(self) -> any:
        """remove and return the smallest element in the min heap"""
        if (len(self.elems) == 0):
            raise RuntimeError("Heap is empty")
        res = self.elems[0]
        self.elems[0] = self.elems[-1]
        del self.elems[-1]
        self._heapify_down()
        return res

    def add(self, item) -> None:
        self.elems.append(item)
        self._heapify_up(len(self.elems) - 1)

    def replace(self, index: int, elem: any) -> None:
        raise NotImplementedError

    def replace_with_condition(self, check: Callable[..., bool], elem: any) -> None:
        for i in range(len(self.elems)):
            if check(self.elems[i]):
                self.replace(i, elem)

    def __str__(self):
        return str(self.elems)


class MinHeap(Heap):
    def _heapify_up(self, start: int) -> None:
        index = start
        while (self._has_parent(index) and self._get_value(self._get_parent_index(index)) > self.elems[index]):
            parent_index = self._get_parent_index(index)
            self.elems[parent_index], self.elems[index] = self.elems[index], self.elems[parent_index]
            index = self._get_parent_index(index)

    def _heapify_down(self, start: int = 0) -> None:
        index = start
        while (self._has_left(index)):
            smaller_child_index = self._get_left_index(index)
            if (self._has_right(index) and self._get_right(index) < self._get_left(index)):
                smaller_child_index = self._get_right_index(index)

            if (self.elems[index] < self.elems[smaller_child_index]):
                return
            self.elems[index], self.elems[smaller_child_index] = \
                self.elems[smaller_child_index], self.elems[index]
            index = smaller_child_index

    def replace(self, index: int, elem: any) -> None:
        self.elems[index] = elem
        if(self._has_parent(index) and self._get_parent(index) > self.elems[index]):
            self._heapify_up(index)
        else:
            self._heapify_down(index)


class MaxHeap(Heap):
    def _heapify_up(self, start: int) -> None:
        index = start
        while (self._has_parent(index) and self._get_value(self._get_parent_index(index)) < self.elems[index]):
            parent_index = self._get_parent_index(index)
            self.elems[parent_index], self.elems[index] = self.elems[index], self.elems[parent_index]
            index = self._get_parent_index(index)

    def _heapify_down(self, start: int = 0) -> None:
        index = start
        while (self._has_left(index)):
            bigger_child_index = self._get_left_index(index)
            if (self._has_right(index) and self._get_right(index) > self._get_left(index)):
                bigger_child_index = self._get_right_index(index)

            if (self.elems[index] > self.elems[bigger_child_index]):
                return
            self.elems[index], self.elems[bigger_child_index] = \
                self.elems[bigger_child_index], self.elems[index]
            index = bigger_child_index

    def replace(self, index: int, elem: any) -> None:
        self.elems[index] = elem
        if(self._has_parent(index) and self._get_parent(index) < self.elems[index]):
            self._heapify_up(index)
        else:
            self._heapify_down(index)

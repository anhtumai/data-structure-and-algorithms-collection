class Node:
    def __init__(self, data: any, _next=None):
        self.data = data
        self.next = _next

    def __str__(self) -> str:
        return str(self.data)


class CircularLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __iter__(self):
        if self.head is None:
            return
        node = self.head
        while True:
            yield node.data
            if node.next != self.head:
                node = node.next
            else:
                break

    def __len__(self):
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = CircularLinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_tail("head")
        >>> len(linked_list)
        1
        >>> linked_list.insert_head("head")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        return len(tuple(iter(self)))

    def __repr__(self):
        """
        String representation/visualization of a Linked Lists
        """
        return "->".join([str(elem) for elem in self]) + "->*"

    def __getitem__(self, index):
        """
        Indexing Support. Used to get value of a node at particular position
        >>> linked_list = CircularLinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> all(str(linked_list[i]) == str(i) for i in range(0, 10))
        True
        >>> linked_list[-10]
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)]
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("List index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def _get_node(self, index: int) -> Node:
        """
        Indexing Support. Used to get a node at particular position
        """
        if not 0 <= index < len(self):
            raise ValueError("List index out of range")
        i = 0
        current = self.head
        while i < index:
            current = current.next
            i += 1
        return current

    def __setitem__(self, index: int, data: any):
        """
        >>> linked_list = CircularLinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> linked_list[0] = 666
        >>> linked_list[0]
        666
        >>> linked_list[5] = -666
        >>> linked_list[5]
        -666
        >>> linked_list[-10] = 666
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)] = 666
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("List index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def __contains__(self, data: any) -> bool:
        for elem in self:
            if (data == elem):
                return True
        return False

    def get_head(self) -> any:
        if self.head:
            return self.head.data
        else:
            raise RuntimeError("List is empty")

    def get_tail_node(self) -> Node:
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            return current
        else:
            raise RuntimeError("List is empty")

    def get_tail(self) -> any:
        return self.get_tail_node().data

    def insert_nth(self, index: int, data: any) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("List index out of range")
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        elif index == 0:
            self.head = Node(data, self.head)
            self.head.next.next = self.head
        else:
            previous_node = self._get_node(index - 1)
            new_node = Node(data, previous_node.next)
            previous_node.next = new_node

    def insert_tail(self, data: any) -> None:
        self.insert_nth(len(self), data)

    def insert_head(self, data: any) -> None:
        self.insert_nth(0, data)

    def delete_nth(self, index: int) -> any:
        if not 0 <= index < len(self):
            raise IndexError("List index out of range")
        if (index == 0):
            deleted_node = self.head
            tail_node = self.get_tail_node()
            self.head = self.head.next
            tail_node.next = self.head
        else:
            previous_node = self._get_node(index - 1)
            deleted_node = previous_node.next
            previous_node.next = deleted_node.next
        return deleted_node.data

    def delete_tail(self) -> any:
        return self.delete_nth(len(self) - 1)

    def delete_head(self) -> any:
        return self.delete_nth(0)

    def stable_reverse(self):
        res = CircularLinkedList()
        for elem in self:
            res.insert_head(elem)
        return res

    def in_place_reverse(self):
        prev = None
        current = self.head
        while True:
            # Store the current node's next node.sss
            next_node = current.next
            # Make the current node's next point backward
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node

            if current == self.head:
                break
        # Return prev in order to put the head at the end
        self.head = prev

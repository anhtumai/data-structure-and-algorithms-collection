class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("List index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index: int, data: any):
        if not 0 <= index < len(self):
            raise ValueError("List index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def head(self) -> Node:
        return self.head

    def tail(self) -> Node:
        return self[len(self) - 1]

    def insert_nth(self, index: int, data: any) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.head.next.prev = self.head
        else:
            previous_node = self.head
            for _ in range(index - 1):
                previous_node = previous_node.next
            new_node.next = previous_node.next
            previous_node.next = new_node

            previous_node.next.prev = previous_node
            if new_node.next is not None:
                new_node.next.prev = new_node

    def insert_tail(self, data: any) -> None:
        self.insert_nth(len(self), data)

    def insert_head(self, data: any) -> None:
        self.insert_nth(0, data)

    def delete_nth(self, index: int) -> any:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index-1):
            current = current.next
        deleted_node = current.next
        current.next = current.next.next

        current.next.prev = current
        return deleted_node.value

    def delete_tail(self) -> any:
        return self.delete_nth(len(self))

    def delete_head(self) -> any:
        return self.delete_nth(0)

    def __str__(self):
        return "<->".join([str(elem) for elem in self])

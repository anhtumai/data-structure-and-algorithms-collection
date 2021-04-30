class Node:
    def __init__(self, data: any):
        self.data = data
        self.next_node = None

    def get_data(self) -> any:
        return self.data

    def get_next(self) -> Node:
        return self.next_node

    def set_next(self, new_node: Node) -> Node:
        self.next_node = new_node


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def head(self) -> Node:
        return self.node

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):

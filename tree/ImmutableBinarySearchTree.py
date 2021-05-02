class BST:
    def is_valid(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def remove(self, data):
        raise NotImplementedError

    def search(self, data):
        raise NotImplementedError


class Empty(BST):
    def is_valid(self) -> bool:
        return True

    def insert(self, data) -> BST:
        return Inode(data)

    def remove(self, data) -> BST:
        return self

    def search(self, data: any) -> BST:
        return self

    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []

    def __str__(self):
        return "Empty"


class Inode(BST):
    def __init__(self, value, left: BST = Empty(), right: BST = Empty()):
        self.value = value
        self.left = left
        self.right = right

    def is_valid(self) -> bool:
        if (isinstance(self.left, Inode) and self.left >= self.value):
            return False
        if (isinstance(self.right, Inode) and self.right <= self.value):
            return False
        return is_valid(self.left) and is_valid(self.right)

    def insert(self, data) -> BST:
        if data == self.value:
            return self
        if (data < self.value):
            return Inode(self.value, self.left.insert(data), self.right)
        return Inode(self.value, self.left, self.right.insert(data))

    def min_value_node(self):
        if (isinstance(self.left, Empty)):
            return self.value
        return self.left.min_value_node()

    def remove(self, data) -> BST:
        if (data < self.value):
            return Inode(self.value, self.left.remove(data), self.right)

        elif (data > self.value):
            return Inode(self.value, self.left, self.right.remove(data))

        else:
            if (isinstance(self.left, Empty) and isinstance(self.right, Empty)):
                return Empty()
            if isinstance(self.left, Empty):
                return self.right
            if isinstance(self.right, Empty):
                return self.left

            min_right = self.right.min_value_node()
            return Inode(min_right, self.left, self.right.remove(min_right))

    def search(self, data: any) -> BST:
        if (data > self.value):
            return self.right.search(data)
        elif (data < self.value):
            return self.left.search(data)
        else:
            return self

    def inorder(self) -> list[any]:
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self) -> list[any]:
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self) -> list[any]:
        return self.left.postorder() + self.right.postorder() + [self.value]

    def __str__(self):
        return "(" + str(self.left) + "<-" + str(self.value) + "->" + str(self.right) + ")"

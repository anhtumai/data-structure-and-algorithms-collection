class TreeNode:
    pass


class Empty(TreeNode):
    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []

    def __str__(self):
        return "Empty"


class Inode(TreeNode):
    def __init__(self, value: any, left: TreeNode = Empty(), right: TreeNode = Empty()):
        self.value = value
        self.left = left
        self.right = right

    def inorder(self) -> list[any]:
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self) -> list[any]:
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self) -> list[any]:
        return self.left.postorder() + self.right.postorder() + [self.value]

    def __str__(self):
        return "(" + str(self.left) + "<-" + str(self.value) + "->" + str(self.right) + ")"

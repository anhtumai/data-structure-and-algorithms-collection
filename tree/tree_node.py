class TreeNode:
    pass

class Empty(TreeNode):
    def __str__(self):
        return "Empty"

class Inode(TreeNode):
    def __init__(self, value: any, left: TreeNode = Empty(), right: TreeNode = Empty()):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "<-" + str(self.value) + "->" + str(self.right) + ")"



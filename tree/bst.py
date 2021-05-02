from tree_node import TreeNode, Inode, Empty


class BST:
    def __init__(self, root: TreeNode = Empty()):
        self.root = root

    def insert(self, data: any) -> bool:
        if(isinstance(self.root, Empty)):
            self.root = Inode(data)
            return True
        return self._recurs_insert(self.root, data)

    def _recurs_insert(self, node: TreeNode, data: any) -> bool:
        if node.value == data:
            return False
        if data > node.value:
            if isinstance(node.right, Empty):
                node.right = Inode(data)
                return True
            else:
                return self._recurs_insert(node.right, data)
        elif data < node.value:
            if isinstance(node.left, Empty):
                node.left = Inode(data)
                return True
            else:
                return self._recurs_insert(node.left, data)
        return

    def search(self, data: any) -> (TreeNode, TreeNode):
        return self._recurs_search(self.root, data, Empty())

    def _recurs_search(self, node: TreeNode, data: any, parent: TreeNode) -> (TreeNode, TreeNode):
        if isinstance(node, Empty):
            return (Empty(), Empty())
        if (data > node.value):
            return self._recurs_search(node.right, data, node)
        elif (data < node.value):
            return self._recurs_search(node.left, data, node)
        else:
            return (node, parent)

    def _recurs_get_min_value(self, node: Inode):
        if isinstance(node.left, Empty):
            return node.value
        return self._recurs_get_min_value(node.left)

    def _is_right(self, node: Inode, parent: Inode) -> bool:
        if (isinstance(parent.right, Empty)):
            return False
        return parent.right.value == node.value

    def _reassign(self, parent: TreeNode, node: Inode, new_node: TreeNode) -> None:
        """
        Mutate the value of a child node, given parent node, child node and its new value
        Note: parent can be Empty, in the case that node in root
        """
        if (isinstance(parent, Empty)):
            self.root = new_node
        else:
            if self._is_right(node, parent):
                parent.right = new_node
            else:
                parent.left = new_node

    def get_node_from_path(self, search_path: list[str]) -> Inode:
        # assume that length of search_path is bigger than 2
        res = self.root
        for state in search_path:
            if state == "E":
                break
            res = res.left if state == "L" else res.right
        return res

    def remove(self, data: any) -> bool:
        node, parent = self.search(data)
        if (isinstance(node, Empty)):
            return False
        if (isinstance(node.left, Empty) and isinstance(node.right, Empty)):
            self._reassign(parent, node, Empty())
        elif (isinstance(node.left, Empty)):
            self._reassign(parent, node, node.right)
        elif (isinstance(node.right, Empty)):
            self._reassign(parent, node, node.left)
        else:
            min_value = self._recurs_get_min_value(node.right)
            if (self.remove(min_value)):
                node.value = min_value
        return True

    def get_inorder(self) -> list[any]:
        return self.root.inorder()

    def get_preorder(self) -> list[any]:
        return self.root.preorder()

    def get_postorder(self) -> list[any]:
        return self.root.postorder()

    def __str__(self):
        return str(self.root)

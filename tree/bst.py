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

    def search(self, data) -> list[str]:
        return self._recurs_search(self.root, data, [])

    def _recurs_search(self, node: TreeNode, data: any, res: list[str]) -> list[str]:
        if isinstance(node, Empty):
            return []
        if (data > node.value):
            return self._recurs_search(node.right, data, res + ["R"])
        elif (data < node.value):
            return self._recurs_search(node.left, data, res + ["L"])
        else:
            return res + ["E"]

    def _recurs_get_min_value(self, node: Inode):
        if isinstance(node.left, Empty):
            return node.value
        return self._recurs_get_min_value(node.left)

    def _is_right(self, node: Inode, parent: Inode) -> bool:
        if (isinstance(parent.right, Empty)):
            return False
        return parent.right.value == node.value

    def _reassign(self, parent, node, new_node):
        # parent can be None, with node is self.root
        if parent:
            if self._is_right(node, parent):
                parent.right = new_node
            else:
                parent.left = new_node
        else:
            self.root = new_node

    def get_node_from_path(self, search_path: list[str]) -> Inode:
        # assume that length of search_path is bigger than 2
        res = self.root
        for state in search_path:
            if state == "E":
                break
            res = res.left if state == "L" else res.right
        return res


    def remove(self, data: any) -> bool:
        search_path: list[str] = self.search(data)
        if (len(search_path) == 0):
            return False
        if (len(search_path) == 1):
            node: Inode = self.root
            parent = None
        else:
            node: Inode = self.get_node_from_path(search_path)
            parent: Inode = self.get_node_from_path(search_path[:-2] + [search_path[-1]])
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

    def __str__(self):
        return str(self.root)

class RBNode:
    pass


class Empty(RBNode):
    def __repr__(self):
        return "Empty"

    def insert(self, data: any) -> RBNode:
        return Inode(data, True, self)

    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []


class Inode(RBNode):
    def __init__(self, value: any, is_red: bool = True, parent: RBNode = Empty(),
                 left: RBNode = Empty(), right: RBNode = Empty()):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.is_red = is_red

    def __repr__(self):
        return f"({self.left}<-{self.value}->{self.right})"

    def get_min_value(self) -> int:
        if (isinstance(self.left, Empty)):
            return self.value
        return self.left.get_min_value()

    def inorder(self) -> list[any]:
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self) -> list[any]:
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self) -> list[any]:
        return self.left.postorder() + self.right.postorder() + [self.value]


class RBTree:
    def __init__(self, root=Empty()):
        self.root = root

    def insert(self, data: any) -> None:
        if (isinstance(self.root, Empty)):
            self.root = Inode(data, is_red=False)
        else:
            self._recurs_insert(self.root, data)

    def _recurs_insert(self, node: RBNode, data: any) -> None:
        """
        Assumption: node cannot be root so node.parent is an Inode
        """
        if (isinstance(node, Empty)):
            parent, is_right = self._get_parent(node)
            new_node = Inode(data, True, parent)
            if is_right:
                parent.right = new_node
            else:
                parent.left = new_node
            self._try_balance(new_node)
        elif (data < node.value):
            self._recurs_insert(node.left, data)
        elif (data > node.value):
            self._recurs_insert(node.right, data)
        else:
            pass

    def _try_balance(self, node: INode) -> None:
        """
        Assumption: node cannot be root so node.parent is an Inode
        """
        parent, is_node_right_child = self._get_parent(node)
        if (isinstance(parent.parent, Empty) or not node.is_red or not parent.is_red):
            return
        grandparent, is_parent_right_child = self._get_parent(parent)
        # Assume grandparent is an Inode
        uncle = grandparent.left if is_parent_right_child else grandparent.right
        if (isinstance(uncle, Empty) or not uncle.is_red):
            # perform rotation
            self.avl_rotate(node, parent, grandparent)
        else:
            parent.is_red = False
            uncle.is_red = False
            if (grandparent != self.root):
                grandparent.is_red = True
                self._try_balance(grandparent)

    def _get_parent(self, node: RBNode) -> tuple[RBNode, bool]:
        if (isinstance(node.parent, Empty)):
            return node.parent, False
        return node.parent, node.parent.right == node

    def avl_rotate(self, node: Inode, parent: Inode, grandparent: Inode) -> None:
        # LR rotation
        if (grandparent.value > parent.value and parent.value < node.value):
            self.ll_rotate(parent)
            self.rr_rotate(grandparent, to_recolor=True)
        # RL rotation
        elif (grandparent.value < parent.value and parent.value > node.value):
            self.rr_rotate(parent)
            self.ll_rotate(grandparent, to_recolor=True)
        # LL rotation
        elif (grandparent.value > parent.value and parent.value > node.value):
            self.ll_rotate(grandparent, to_recolor=True)
        # RR rotation
        else:
            self.rr_rotate(grandparent, to_recolor=True)

    def ll_rotate(self, a: Inode, to_recolor: bool = False) -> None:
        """Perform left left rotation
            a: grandparent, b: parent, c: node
            Before:
                     a
                    / \
                   b  ar
                  / \
                 c  br
            After:
                    b
                   / \
                  c   a
                     / \
                    br  ar
        """

        b = a.left
        br = b.right

        b.right = a
        a.left = br

        if to_recolor:
            b.is_red, a.is_red, c.is_red = False, True, True

        parent, is_right = self._get_parent(a)
        if is_right:
            parent.right = b
        else:
            parent.left = b

    def rr_rotate(self, a: Inode, to_recolor: bool = False) -> None:
        """Perform right right rotation
            Before:
                    a
                   / \
                  al  b
                     / \
                    bl  c
            After:
                    b
                   / \
                  a   c
                 / \
                al bl
        """

        b = a.right
        bl = b.left

        b.left = a
        a.right = bl

        if to_recolor:
            b.is_red, a.is_red, c.is_red = False, True, True

        parent, is_right = self._get_parent(a)
        if is_right:
            parent.right = b
        else:
            parent.left = b

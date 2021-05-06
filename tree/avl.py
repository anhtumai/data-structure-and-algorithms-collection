class AVLNode:
    def get_height(self):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError


class Empty(AVLNode):
    def __init__(self):
        self.height = 0

    def __repr__(self):
        return "Empty"

    def calculate_height(self) -> int:
        return 0

    def get_balance(self) -> int:
        return 0

    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []


class Inode(AVLNode):
    def __init__(self, value: any):
        self.value = value
        self.left = Empty()
        self.right = Empty()
        self.update_height()

    def __repr__(self):
        return f"({self.left}<-{self.value}->{self.right})"

    def update_height(self) -> None:
        self.height = self.calculate_height()

    def calculate_height(self) -> int:
        return 1 + max(self.left.calculate_height(), self.right.calculate_height())

    def get_balance(self) -> int:
        return self.left.height - self.right.height

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


class AVLTree:

    def __init__(self, root: AVLNode = Empty()):
        self.root = root

    def __repr__(self):
        return str(self.root)

    def insert(self, data: any) -> bool:
        is_inserted, self.root = self._recurs_insert(self.root, data)
        return is_inserted

    def _recurs_insert(self, node: AVLNode, data: any) -> tuple[bool, AVLNode]:
        """Recursively insert element to AVL tree
            Args:
                node: AVL node
                data: what need inserting in the AVL tree
            Returns:
                is_inserted: True means data is successfully inserted,
                             False means data already existed in the tree
                node: new node after inserting new data
        No duplicated data is allowed since it will cause trouble for deleting node by value.
        """
        if (isinstance(node, Empty)):
            return True, Inode(data)
        if (data < node.value):
            is_inserted, node.left = self._recurs_insert(node.left, data)
        elif (data > node.value):
            is_inserted, node.right = self._recurs_insert(node.right, data)
        else:
            return False, node.right

        node.update_height()
        balance = node.get_balance()

        # when balance > 1, node.left and node.left.left must be a leaf
        # perform LL rotation
        if (balance > 1 and data < node.left.value):
            return is_inserted, self.ll_rotate(node)

        # perform RR rotation
        if (balance < -1 and data > node.right.value):
            return is_inserted, self.rr_rotate(node)

        # perform RL rotation
        if (balance < -1 and data < node.right.value):
            node.right = self.ll_rotate(node.right)
            return is_inserted, self.rr_rotate(node)

        # perform LR rotation
        if (balance > 1 and data > node.left.value):
            node.left = self.rr_rotate(node.left)
            return is_inserted, self.ll_rotate(node)

        return is_inserted, node

    def remove(self, data: any) -> bool:
        is_removed, self.root = self._recurs_remove(self.root, data)
        return is_removed

    def _recurs_remove(self, node: AVLNode, data: any) -> tuple[bool, AVLNode]:
        if (isinstance(node, Empty)):
            return False, Empty()

        if (data < node.value):
            is_removed, node.left = self._recurs_remove(node.left, data)

        elif (data > node.value):
            is_removed, node.right = self._recurs_remove(node.right, data)

        else:
            if (isinstance(node.left, Empty) and isinstance(node.right, Empty)):
                return True, Empty()
            if isinstance(node.left, Empty):
                return True, node.right
            if isinstance(node.right, Empty):
                return True, node.left

            min_right = node.right.get_min_value()
            node.value = min_right
            is_removed, node.right = self._recurs_remove(
                node.right, min_right)

        node.update_height()
        balance = node.get_balance()

        # LL rotation
        if (balance > 1 and node.left.get_balance() >= 0):
            return is_removed, self.ll_rotate(node)

        # LR rotation
        if (balance > 1 and node.left.get_balance() < 0):
            node.left = self.rr_rotate(node.left)
            return is_removed, self.ll_rotate(node)

        # RR rotation
        if (balance < -1 and node.right.get_balance() <= 0):
            return is_removed, self.rr_rotate(node)

        # RL rotation
        if (balance < -1 and node.right.get_balance() > 0):
            node.right = self.ll_rotate(node.right)
            return is_removed, self._rotate(node)

        return is_removed, node

    def ll_rotate(self, a: Inode) -> Inode:
        """Perform left left rotation
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

        return b

    def rr_rotate(self, a: Inode) -> Inode:
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

        return b

    def get_inorder(self) -> list[any]:
        return self.root.inorder()

    def get_preorder(self):
        return self.root.preorder()

    def get_postorder(self):
        return self.root.postorder()

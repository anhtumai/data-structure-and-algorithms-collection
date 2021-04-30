from tree_node import TreeNode, Inode, Empty

class AVLNode:
    def get_height(self):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError


class Empty(AVLNode):
    def get_height(self) -> int:
        return 0

    def get_balance(self) -> int:
        return 0

    def __str__(self):
        return "Empty"


class Inode(AVLNode):
    def __init__(self, value: any):
        self.value = value
        self.left = Empty()
        self.right = Empty()

    def get_height(self) -> int:
        return 1 + max(self.left.get_height(), self.right.get_height())

    def get_balance(self) -> int:
        return self.left.get_height() - self.right.get_height()

    def get_min_value(self) -> int:
        if (isinstance(self.left, Empty)):
            return self.value
        return self.left.get_min_value()

    def __str__(self):
        return f"({self.left}<-{self.value}->{self.right})"


class AVLTree:

    def insert(self, node: AVLNode, value: any) -> AVLNode:
        if (isinstance(node, Empty)):
            return Inode(value)
        if (value < node.value):
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.update_height()

        balance = node.get_balance()

        # when balance > 1, node.left and node.left.left must be a leaf
        # perform LL rotation
        if (balance > 1 and value < node.left.value):
            return self.ll_rotate(node)

        # perform RR rotation
        if (balance < -1 and value > node.right.value):
            return self.rr_rotate(node)

        # perform RL rotation
        if (balance < -1 and value < node.right.value):
            node.right = self.ll_rotate(node.right)
            return self.rr_rotate(node)

        # perform LR rotation
        if (balance > 1 and value > node.left.value):
            node.left = self.rr_rotate(node.left)
            return self.ll_rotate(node)

        return node

    def remove(self, node: AVLNode, value: any) -> AVLNode:
        if (isinstance(node, Empty)):
            return Empty()

        if (value < node.value):
            node.left = self.remove(node.left, value)

        elif (value > node.value):
            node.right = self.remove(node.right, value)

        else:
            if (isinstance(node.left, Empty) and isinstance(node.right, Empty)):
                return Empty()
            if isinstance(node.left, Empty):
                return node.right
            if isinstance(node.right, Empty):
                return node.left

            min_right = node.right.get_min_value()
            node.value = min_right
            node.right = self.remove(node.right, min_right)

        node.update_height()

        balance = node.get_balance()

        # LL rotation
        if (balance > 1 and node.left.get_balance() >= 0):
            return self.ll_rotate(node)

        # LR rotation
        if (balance > 1 and node.left.get_balance() < 0):
            node.left = self.rr_rotate(node.left)
            return self.ll_rotate(node)

        # RR rotation
        if (balance < -1 and node.right.get_balance() <= 0):
            return self.rr_rotate(node)

        # RL rotation
        if (balance < -1 and node.right.get_balance() > 0):
            node.right = self.ll_rotate(node.right)
            return self._rotate(node)

        return node

    def ll_rotate(self, a: Inode) -> Inode:
        """Assume that a.left / b and a.left.left / c are leaves
            Before: (c<-b->br)<-a->ar
            After:  c<-b->(br<-a->ar)
        """
        b = a.left
        br = b.right

        b.right = a
        a.left = br

        return b

    def rr_rotate(self, a: Inode) -> Inode:
        """Assume that a.right / b and a.right.right / c are leaves
            Before: al<-a->(bl<-b->c)
            After:  (al<-a->bl)<-b->c
        """

        b = a.right
        bl = b.left

        b.left = a
        a.right = bl

        return b

class AVLNode:
    def calculate_height(self):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError


class Empty(AVLNode):

    def __init__(self):
        self.height = 0

    def __repr__(self):
        return "Empty"

    def calculate_height(self):
        return 0

    def get_balance(self):
        return 0

    def insert(self, value: any) -> AVLNode:
        return Inode(value)

    def remove(self, value: any) -> AVLNode:
        return Empty()

    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []


class Inode(AVLNode):
    def __init__(self, value: any, left: AVLNode = Empty(), right: AVLNode = Empty()):
        self.value = value
        self.left = left
        self.right = right
        self.height = self.calculate_height()

    def __repr__(self):
        return f"({self.left}<-{self.value}->{self.right})"

    def calculate_height(self) -> int:
        return 1 + max(self.left.height, self.right.height)

    def get_balance(self) -> int:
        return self.left.height - self.right.height

    def get_min_value(self) -> int:
        if (isinstance(self.left, Empty)):
            return self.value
        return self.left.get_min_value()

    def insert(self, value: any) -> AVLNode:
        if (value < self.value):
            res = Inode(self.value, self.left.insert(value), self.right)
        else:
            res = Inode(self.value, self.left, self.right.insert(value))

        balance = res.get_balance()

        # when balance > 1, self.left and self.left.left must be a leaf
        # perform LL rotation
        if (balance > 1 and value < res.left.value):
            return res.ll_rotate()

        # perform RR rotation
        if (balance < -1 and value > res.right.value):
            return res.rr_rotate()

        # perform RL rotation
        if (balance < -1 and value < res.right.value):
            return res.rl_rotate()

        # perform LR rotation
        if (balance > 1 and value > res.left.value):
            return res.lr_rotate()

        return res

    def remove(self, value: any) -> AVLNode:
        if (value < self.value):
            res = Inode(self.value, self.left.remove(value), self.right)

        elif (value > self.value):
            res = Inode(self.value, self.left, self.right.remove(value))

        else:
            if (isinstance(self.left, Empty) and isinstance(self.right, Empty)):
                return Empty()
            elif isinstance(self.left, Empty):
                return self.right
            elif isinstance(self.right, Empty):
                return self.left

            else:
                min_right = self.right.get_min_value()
                res = Inode(min_right, self.left, self.right.remove(min_right))
        balance = res.get_balance()

        # LL rotation
        if (balance > 1 and res.left.get_balance() >= 0):
            return res.ll_rotate()

        # LR rotation
        if (balance > 1 and res.left.get_balance() < 0):
            return res.lr_rotate()

        # RR rotation
        if (balance < -1 and res.right.get_balance() <= 0):
            return res.rr_rotate()

        # RL rotation
        if (balance < -1 and res.right.get_balance() > 0):
            return res.rl_rotate()

        return res

    def ll_rotate(self) -> AVLNode:
        """Perform left left rotation (assume self is a)
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
        b = self.left
        c = b.left
        return Inode(b.value, c, Inode(self.value, b.right, self.right))

    def rr_rotate(self) -> AVLNode:
        """Perform right right rotation (assume self is a)
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

        b = self.right
        c = b.right
        return Inode(b.value, Inode(self.value, self.left, b.left), c)

    def rl_rotate(self) -> AVLNode:
        b = self.right
        c = b.left
        return Inode(c.value, Inode(self.value, self.left, c.left), Inode(b.value, c.right, b.left))

    def lr_rotate(self) -> AVLNode:
        b = self.left
        c = b.right
        return Inode(c.value, Inode(b.value, b.left, c.left), Inode(self.value, c.right, self.right))

    def inorder(self) -> list[any]:
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self) -> list[any]:
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self) -> list[any]:
        return self.left.postorder() + self.right.postorder() + [self.value]

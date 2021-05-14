from sty import fg, bg, ef, rs
import sys


class RBNode:
    pass


class Empty(RBNode):

    def __init__(self, parent: "Inode"):
        self.parent = parent
        self.is_red = False

    def is_black(self) -> bool:
        return True

    def __repr__(self):
        return "Empty"

    def inorder(self) -> list[any]:
        return []

    def preorder(self) -> list[any]:
        return []

    def postorder(self) -> list[any]:
        return []


class Inode(RBNode):
    def __init__(self, value: any, is_red: bool, parent: RBNode,
                 left: RBNode = None, right: RBNode = None):
        self.value = value
        self.parent = parent
        # If left or right is None, assign Empty node
        self.left = left if left else Empty(self)
        self.right = right if right else Empty(self)
        self.is_red = is_red

    def is_black(self) -> bool:
        return not self.is_red

    def __repr__(self):
        colour_start = fg.red if self.is_red else ""
        colour_end = fg.rs if self.is_red else ""
        return f"({self.left}<-{colour_start}{self.value}{colour_end}->{self.right})"

    def inorder(self) -> list[any]:
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self) -> list[any]:
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self) -> list[any]:
        return self.left.postorder() + self.right.postorder() + [self.value]


class RBTree:
    def __init__(self, root=Empty(None)):
        self.root = root

    def __repr__(self):
        return str(self.root)

    def __contains__(self, data: any) -> bool:
        return isinstance(self.find_node_by_value(data), Inode)

    def insert(self, data: any) -> None:
        if (isinstance(self.root, Empty)):
            self.root = Inode(data, is_red=False, parent=None)
        else:
            self._recurs_insert(self.root, data)

    def _recurs_insert(self, node: RBNode, data: any) -> None:
        """
        Assumption: root is Inode so parent of Empty node is always Inode
        """

        if (isinstance(node, Empty)):
            parent, is_right = self._get_parent(node)
            new_node = Inode(data, is_red=True, parent=parent)
            if is_right:
                parent.right = new_node
            else:
                parent.left = new_node
            self._fix_insert(new_node)
            return
        if (data < node.value):
            self._recurs_insert(node.left, data)
        elif (data > node.value):
            self._recurs_insert(node.right, data)

    def _fix_insert(self, node: Inode) -> None:
        """
        Assumption: node cannot be root so node.parent is an Inode
        """
        parent, is_node_right_child = self._get_parent(node)
        grandparent, is_parent_right_child = self._get_parent(parent)
        if (grandparent is None  # when parent is root
                or not (node.is_red and parent.is_red)):
            return

        uncle = grandparent.left if is_parent_right_child else grandparent.right

        # Perform suitable rotation and recolor if uncle is black or Empty node
        if (isinstance(uncle, Empty) or not uncle.is_red):
            self.avl_rotate(node, parent, grandparent)
        # Recolor and recheck if uncle is red
        else:
            parent.is_red = False
            uncle.is_red = False
            if (grandparent != self.root):
                grandparent.is_red = True
                self._fix_insert(grandparent)

    def _get_parent(self, node: RBNode) -> tuple[RBNode, bool]:
        if not node.parent:  # node is root
            return node.parent, False
        return node.parent, node.parent.right == node

    def _get_sibling(self, node: RBNode) -> tuple[RBNode, bool]:
        if not node.parent:  # node is root
            return None, False
        if node.parent.right == node:
            return node.parent.left, False
        else:
            return node.parent.right, True

    def avl_rotate(self, node: Inode, parent: Inode, grandparent: Inode) -> None:
        # LR rotation
        if (grandparent.value > parent.value and parent.value < node.value):
            self.rr_rotate(parent)
            self.ll_rotate(grandparent, to_recolor=True)
        # RL rotation
        elif (grandparent.value < parent.value and parent.value > node.value):
            self.ll_rotate(parent)
            self.rr_rotate(grandparent, to_recolor=True)
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
        parent, is_right = self._get_parent(a)

        b = a.left
        br = b.right

        b.right = a
        a.left = br

        # Update parent
        b.parent = parent
        a.parent = b
        br.parent = a

        if parent:
            if is_right:
                parent.right = b
            else:
                parent.left = b
        else:  # parent is None if the node we need to rotate is root
            self.root = b

        if to_recolor:
            c = b.left
            b.is_red, a.is_red, c.is_red = False, True, True

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

        parent, is_right = self._get_parent(a)

        b = a.right
        bl = b.left

        b.left = a
        a.right = bl

        # Update parent
        b.parent = parent
        a.parent = b
        bl.parent = a

        if parent:
            if is_right:
                parent.right = b
            else:
                parent.left = b
        else:
            self.root = b

        if to_recolor:
            c = b.right
            b.is_red, a.is_red, c.is_red = False, True, True

    def find_node_by_value(self, data: any) -> RBNode:
        """
            Return:
                Empty if data is not found in the tree
                or Inode containing data
        """
        def _find_node_by_value(node: RBNode) -> RBNode:
            if (isinstance(node, Empty)):
                return node
            if node.value == data:
                return node
            elif data > node.value:
                return _find_node_by_value(node.right)
            else:
                return _find_node_by_value(node.left)
        return _find_node_by_value(self.root)

    def _get_node_with_smallest_value(self, node: Inode) -> Inode:
        if (isinstance(node.left, Empty)):
            return node
        else:
            return self._get_node_with_smallest_value(node.left)

    def remove(self, data: any) -> bool:
        """
            Return:
                False if data has already existed
                True if data is successfully inserted
        """
        deleted_node = self.find_node_by_value(data)
        if (isinstance(deleted_node, Empty)):
            return False
        if (isinstance(deleted_node.left, Inode) and
                isinstance(deleted_node.right, Inode)):
            successor = self._get_node_with_smallest_value(
                deleted_node.right)
            deleted_node.value = successor.value
            deleted_node = successor

        # remove node with 0 or 1 children
        self._remove_node_without_2_children(deleted_node)
        return True

    def _remove_leaf(self, leaf: Inode) -> None:
        """Leaf is an Inode without any children"""
        if (isinstance(leaf.left, Inode) or isinstance(leaf.right, Inode)):
            raise RuntimeError("Leaf has child, wtf is this")
        # if leaf is root
        if leaf == self.root:
            self.root = Empty(None)
        elif leaf == leaf.parent.right:
            leaf.parent.right = Empty(leaf.parent)
        else:
            leaf.parent.left = Empty(leaf.parent)

    def _remove_node_without_2_children(self, node: Inode) -> None:
        """
        Assumption: node has 0 or 1 child.
        """
        not_nil_child = node.right if isinstance(
            node.left, Empty) else node.left
        if node == self.root:
            self.root = not_nil_child
            self.root.parent = None
            self.root.is_red = False
            return
        if node.is_red:
            # Red node cannot have any children
            # Because if red node has 1 black node in 1 side,
            # then the number of black node is imbalance
            self._remove_leaf(node)
        else:
            # Black node has only 1 child, and that child must be red
            if (not_nil_child.is_red):
                node.value = not_nil_child.value
                node.left = not_nil_child.left
                node.right = not_nil_child.right
            else:
                # In this situation, we can be sure that
                # deleted node is black
                # it has 0 child
                # 6 cases
                self._remove_double_black_node(node)

    def _remove_double_black_node(self, node: Inode) -> None:
        """
        Big case: deleted node is black and its child is also black.
        -> Double black node case
        Loop through each case recursively.
        Assumption: this black node only doesn't have any child.
        (Because if it has 1 child then that child must be red)
        """
        # Actual remove something
        parent, is_right = self._get_parent(node)
        new_node = Empty(parent)

        if is_right:
            parent.right = new_node
        else:
            parent.left = new_node

        # Remove double black mark (no node is removed in this phase)
        self._fix_double_black_remove(new_node)

    def _fix_double_black_remove(self, node: RBNode) -> None:
        # Case 1: node is root
        if self.root == node:
            node.is_red = False
            return
        sibling, is_sibling_right = self._get_sibling(node)
        parent, _ = self._get_parent(node)
        closer_child = sibling.left if is_sibling_right else sibling.right
        outer_child = sibling.right if is_sibling_right else sibling.left
        if (
            sibling.is_black() and
            sibling.left.is_red and
            sibling.right.is_red
        ):
            self.__case_2(parent, sibling, is_sibling_right)
        elif (
            sibling.is_black() and
            sibling.left.is_black() and
            sibling.right.is_black()
        ):
            self.__case_3(parent, sibling, is_sibling_right)
        elif (sibling.is_red):
            self.__case_4(parent, sibling, node, is_sibling_right)
        elif (
            sibling.is_black() and
            closer_child.is_red and
            outer_child.is_black()
        ):
            self.__case_5(sibling, node, closer_child,
                          outer_child, is_sibling_right)
        elif (
            sibling.is_black() and
            closer_child.is_black() and
            outer_child.is_red
        ):
            self.__case_6(parent, sibling, is_sibling_right)

    def __case_2(self, parent: Inode, sibling: Inode, is_sibling_right: bool):
        """
        Case 2 applies when
            sibling is Black
            sibling children are Red
                 30B                                 40B
                /   \     --CASE 2 ROTATE-->        /   \
              |N|   40B     Parent rotate         30B   50B
                    /  \    to double-black         \
                  35R  50R                          35R
        """
        sibling.is_red, parent.is_red = parent.is_red, sibling.is_red
        if is_sibling_right:
            sibling.right.is_red = False
            self.rr_rotate(parent)
        else:
            sibling.left.is_red = False
            self.ll_rotate(parent)

    def __case_3(self, parent: Inode, sibling: Inode, is_sibling_right: bool) -> None:
        """
        Case 3 applies when
            sibling is Black
            sibling children are Black or Empty
                 30B                                 |30B|
                /   \     --CASE 3 RECOLOR-->        /   \
              |N|   40B     Recolor parent and      N    40R
                    /  \    sibling.
                   N    N
        If parent is Black initially, it will be come double black.
        Need to apply fix double black on parent
        """
        if parent.is_red:
            parent.is_red = False
            sibling.is_red = True
        else:  # now parent become double black
            parent.is_red = False
            sibling.is_red = True
            self._fix_double_black_remove(parent)

    def __case_4(self, parent: Inode, sibling: Inode, node: RBNode, is_sibling_right: bool) -> None:
        """
        Case 4 applies when
            sibling is Red
            sibling children are Black or Empty
                 30B                                    40B
                /   \     --CASE 4 ROTATE-->           /   \
              |N|   40R     Rotate parent            30R   50B
                    /  \    toward double black     /  \
                  35B  50B                        |N|  35B
        Reapply fix double black on empty node
        """
        sibling.is_red, parent.is_red = parent.is_red, sibling.is_red
        # Rotate parent toward double black direction
        if is_sibling_right:
            self.rr_rotate(parent)
        else:
            self.ll_rotate(parent)
        self._fix_double_black_remove(node)

    def __case_5(self, sibling: Inode, node: RBNode,
                 closer_child: RBNode, outer_child: RBNode,
                 is_sibling_right: bool) -> None:
        """
        Case 5 applies when
            sibling is Black
            closer sibling child is Red
            outer sibling child is Black or Empty
                  10B                                      10B
                /     \     --CASE 5 ROTATE-->           /     \
              |5B|    30B     Rotate sibling           |5B|    25B
              /  \    /  \    opposite double black    /  \    /  \
             N   7B 25R  40B                          N   7B  20B 30R
                    /  \                                          /  \
                   20B 28B                                       28B 40B
        After this apply case 6
        """
        sibling.is_red, closer_child.is_red = closer_child.is_red, sibling.is_red
        if is_sibling_right:
            self.ll_rotate(sibling)
        else:
            self.rr_rotate(sibling)
        self._fix_double_black_remove(node)

    def __case_6(self, parent: Inode, sibling: Inode, is_sibling_right: bool) -> None:
        """
        Case 6 applies when
            sibling is Black
            closer sibling child is Black or Empty
            outer sibling child is Red
                  10B                                      25B
                /     \     --CASE 5 ROTATE-->           /     \
              |5B|    25B     Rotate parent            10B     30B
              /  \    /  \    to double black          /  \    /  \
             N   7B 20B  30R                          5B  20B 28B 40B
                         /  \                          \
                        28B  40B                       7R
        """
        parent.is_red, sibling.is_red = sibling.is_red, parent.is_red
        if is_sibling_right:
            self.rr_rotate(parent)
        else:
            self.ll_rotate(parent)
        sibling.left.is_red = False
        sibling.right.is_red = False

    def get_inorder(self) -> list[any]:
        return self.root.inorder()

    def get_preorder(self) -> list[any]:
        return self.root.preorder()

    def get_postorder(self) -> list[any]:
        return self.root.postorder()

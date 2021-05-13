from sty import fg, bg, ef, rs


class RBNode:
    pass


class Empty(RBNode):

    def __init__(self, parent: "Inode"):
        self.parent = parent
        self.is_red = False

    def is_black(self) -> bool:
        return False

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

    def get_min_value(self) -> any:
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
    def __init__(self, root=Empty(None)):
        self.root = root

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

    def find_node_by_value(self, data: any):
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

    def remove(self, data: any) -> None:
        deleted_node = self.find_node_by_value(data)
        if (isinstance(deleted_node, Empty)):
            return  # will return false
        if (isinstance(deleted_node.left, Inode) and
                isinstance(deleted_node.right, Inode)):
            successor = self._get_node_with_smallest_value(
                deleted_node.right)
            deleted_node.value = successor.value
            deleted_node = successor

        # remove node with 0 or 1 children
        self._remove_node_without_2_children(deleted_node)

    def _remove_leaf(self, leaf: Inode) -> None:
        """Leaf is an Inode without any children"""
        if (isinstance(leaf.left, Inode) or isinstance(leaf.right, Inode)):
            raise RuntimeError("Leaf has child, wtf is this")
        # if leaf is root
        if leaf == self.root:
            self.root = Empty(None)
        elif leaf.value > leaf.parent.value:
            leaf.parent.right = Empty(leaf.parent)
        else:
            leaf.parent.left = Empty(leaf.parent)

    def _remove_node_without_2_children(self, node: Inode) -> None:
        """
        Assumption: node has 0 or 1 child.
        """
        not_nil_child = node.left if not isinstance(
            node.left, Empty) else node.right
        if node == self.root:
            self.root = not_nil_child
            self.root.parent = None
            self.root.is_red = False
            return
        if node.is_red:
            # Assume that red node cannot have any children
            self._remove_leaf(node)
        else:
            if (isinstance(not_nil_child, Inode) and not_nil_child.is_red):
                node.value = not_nil_child.value
                node.left = not_nil_child.left
                node.right = not_nil_child.right
            else:
                # 6 cases
                self._remove_double_black_node(node)

    def _remove_double_black_node(self, node: Inode) -> None:
        """
        Loop through each case recursively until we reach a terminating case.
        What we're left with is a leaf node which is ready to be deleted without consequences
        """
        self.__case_1(node)
        self._remove_leaf(node)

    def __case_1(self, node):
        """
        Case 1 is when there's a double black node on the root
        Because we're at the root, we can simply remove it
        and reduce the black height of the whole tree.
            __|10B|__                  __10B__
           /         \      ==>       /       \
          9B         20B            9B        20B
        """
        if self.root == node:
            node.is_red = False
            return
        self.__case_2(node)

    def __case_2(self, node):
        """
        Case 2 applies when
            the parent is BLACK
            the sibling is RED
            the sibling's children are BLACK or NIL
        It takes the sibling and rotates it
                         40B                                              60B
                        /   \       --CASE 2 ROTATE-->                   /   \
                    |20B|   60R       LEFT ROTATE                      40R   80B
    DBL BLACK IS 20----^   /   \      SIBLING 60R                     /   \
                         50B    80B                                |20B|  50B
            (if the sibling's direction was left of it's parent, we would RIGHT ROTATE it)
        Now the original node's parent is RED
        and we can apply case 4 or case 6
        """
        parent = node.parent
        sibling, is_sibling_right = self._get_sibling(node)
        if (sibling.is_red and
            (not parent.is_red) and
            (isinstance(sibling.left, Empty) or not sibling.left.is_red) and
                (isinstance(sibling.right, Empty) or not sibling.right.is_red)):
            if is_sibling_right:
                self.rr_rotate(parent)
            else:
                self.ll_rotate(parent)

            parent.is_red = True
            sibling.is_red = False
            return self.__case_1(node)
        self.__case_3(node)

    def __case_3(self, node):
        """
        Case 3 deletion is when:
            the parent is BLACK
            the sibling is BLACK
            the sibling's children are BLACK
        Then, we make the sibling red and
        pass the double black node upwards
                            Parent is black
               ___50B___    Sibling is black                       ___50B___
              /         \   Sibling's children are black          /         \
           30B          80B        CASE 3                       30B        |80B|  Continue with other cases
          /   \        /   \        ==>                        /  \        /   \
        20B   35R    70B   |90B|<---REMOVE                   20B  35R     70R   X
              /  \                                               /   \
            34B   37B                                          34B   37B
        """
        parent = node.parent
        sibling, _ = self._get_sibling(node)
        if (sibling.is_black() and
            parent.is_black() and
            (isinstance(sibling.left, Empty) or sibling.left.is_black()) and
                (isinstance(sibling.right, Empty) or sibling.right.is_black())):
            # color the sibling red and forward the double black node upwards
            # (call the cases again for the parent)
            sibling.is_red = True
            return self.__case_1(parent)  # start again

        self.__case_4(node)

    def __case_4(self, node):
        """
        If the parent is red and the sibling is black with no red children,
        simply swap their colors
        DB-Double Black
                __10R__                   __10B__        The black height of the left subtree has been incremented
               /       \                 /       \       And the one below stays the same
             DB        15B      ===>    X        15R     No consequences, we're done!
                      /   \                     /   \
                    12B   17B                 12B   17B
        """
        parent = node.parent
        if parent.is_red:
            sibling, _ = self._get_sibling(node)
            if (sibling.is_black() and
                (isinstance(sibling.left, Empty) or sibling.left.is_black()) and
                    (isinstance(sibling.right, Empty) or sibling.right.is_black())):
                parent.is_red, sibling.is_red = sibling.is_red, parent.is_red  # switch colors
                return  # Terminating
        self.__case_5(node)

    def __case_5(self, node):
        """
        Case 5 is a rotation that changes the circumstances so that we can do a case 6
        If the closer node is red and the outer BLACK or NIL, we do a left/right rotation, depending on the orientation
        This will showcase when the CLOSER NODE's direction is RIGHT
              ___50B___                                                    __50B__
             /         \                                                  /       \
           30B        |80B|  <-- Double black                           35B      |80B|        Case 6 is now
          /  \        /   \      Closer node is red (35R)              /   \      /           applicable here,
        20B  35R     70R   X     Outer is black (20B)               30R    37B  70R           so we redirect the node
            /   \                So we do a LEFT ROTATION          /   \                      to it :)
          34B  37B               on 35R (closer node)           20B   34B
        """
        sibling, is_sibling_right = self._get_sibling(node)
        closer_node = sibling.left if is_sibling_right else sibling.right
        outer_node = sibling.right if is_sibling_right else sibling.left
        if ((isinstance(closer_node, Inode) and closer_node.is_red) and
            (isinstance(outer_node, Empty) or outer_node.is_black()) and
                sibling.is_black()):
            if is_sibling_right:
                self.ll_rotate(sibling)
            else:
                self.rr_rotate(sibling)
            closer_node.is_red = False
            sibling.is_red = True

        self.__case_6(node)

        self.__case_6(node)

    def __case_6(self, node):
        """
        Case 6 requires
            SIBLING to be BLACK
            OUTER NODE to be RED
        Then, does a right/left rotation on the sibling
        This will showcase when the SIBLING's direction is LEFT
                            Double Black
                    __50B__       |                               __35B__
                   /       \      |                              /       \
      SIBLING--> 35B      |80B| <-                             30R       50R
                /   \      /                                  /   \     /   \
             30R    37B  70R   Outer node is RED            20B   34B 37B    80B
            /   \              Closer node doesn't                           /
         20B   34B                 matter                                   70R
                               Parent doesn't
                                   matter
                               So we do a right rotation on 35B!
        """
        sibling, is_sibling_right = self._get_sibling(node)
        outer_node = sibling.right if is_sibling_right else sibling.left

        if (sibling.is_black() and
                (isinstance(outer_node, Inode) and outer_node.is_red)):
            is_parent_red = sibling.parent.is_red
            if is_sibling_right:
                self.rr_rotate(sibling.parent)
            else:
                self.ll_rotate(sibling.parent)
            sibling.is_red = is_parent_red
            sibling.right.is_red = False
            sibling.left.is_red = False

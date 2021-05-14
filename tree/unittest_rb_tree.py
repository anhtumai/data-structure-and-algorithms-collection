# Original of test: based on https://www.youtube.com/watch?v=qA02XWRTBdw

import unittest
from red_black_tree import RBNode, Empty, Inode, RBTree
import random


def generate_tree(elems: list[any]) -> RBTree:
    res = RBTree()
    for elem in elems:
        res.insert(elem)
    return res


def verify_red_black_tree(tree: RBTree) -> bool:
    if (isinstance(tree.root, Inode) and tree.root.is_red):
        return False
    # On going implementation


class TestElem(unittest.TestCase):
    def test_insert(self):
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.get_inorder(),
                         [1, 2, 7, 10, 15, 16, 18, 25, 30, 40, 60, 70])
        self.assertEqual(tree1.get_preorder(), [
                         16, 10, 2, 1, 7, 15, 25, 18, 40, 30, 60, 70])
        for x in xs:
            if x in [1, 7, 40, 70]:
                self.assertEqual(tree1.find_node_by_value(x).is_red, True)
            else:
                self.assertEqual(tree1.find_node_by_value(x).is_black(), True)

    def test_delete_all(self):

        for i in range(0, 2000):
            insert_elems = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
            tree1 = generate_tree(insert_elems)
            remove_elems = insert_elems.copy()
            random.shuffle(remove_elems)
            for elem in remove_elems:
                self.assertEqual(elem in tree1, True)
                tree1.remove(elem)
                self.assertEqual(elem in tree1, False)
            self.assertIsInstance(tree1.root, Empty)


if __name__ == "__main__":
    unittest.main()

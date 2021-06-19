# Original of test: based on https://www.youtube.com/watch?v=qA02XWRTBdw

import unittest
from red_black_tree import RBNode, Empty, Inode, RBTree
import random


def generate_tree(elems: list[any]) -> RBTree:
    res = RBTree()
    for elem in elems:
        res.insert(elem)
    return res


class TestElem(unittest.TestCase):
    def test_insert(self):
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(
            tree1.get_inorder(), [1, 2, 7, 10, 15, 16, 18, 25, 30, 40, 60, 70]
        )
        self.assertEqual(
            tree1.get_preorder(), [16, 10, 2, 1, 7, 15, 25, 18, 40, 30, 60, 70]
        )
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

    def test_delete_case1(self):
        """The removed node is root node"""
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 16)
        tree1.remove(16)
        self.assertEqual(tree1.get_inorder(), [1, 2, 7, 10, 15, 18, 25, 30, 40, 60, 70])
        self.assertEqual(
            tree1.get_preorder(), [18, 10, 2, 1, 7, 15, 40, 25, 30, 60, 70]
        )
        for x in [1, 7, 30, 70]:
            self.assertEqual(tree1.find_node_by_value(x).is_red, True)

        tree1.remove(18)
        self.assertEqual(tree1.get_preorder(), [25, 10, 2, 1, 7, 15, 40, 30, 60, 70])
        self.assertEqual(tree1.get_inorder(), [1, 2, 7, 10, 15, 25, 30, 40, 60, 70])

    def test_delete_case2(self):
        """After removal, the sibling of double black has 2 red children"""
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 16)
        tree1.remove(15)
        self.assertEqual(tree1.get_inorder(), [1, 2, 7, 10, 16, 18, 25, 30, 40, 60, 70])
        self.assertEqual(
            tree1.get_preorder(), [16, 2, 1, 10, 7, 25, 18, 40, 30, 60, 70]
        )

    def test_delete_case3(self):
        """After removal, the sibling of double black is red and has 0 or 2 black children"""
        xs = [10, 5, 30, 2, 7, 25, 40]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 10)
        tree1.remove(40)
        self.assertEqual(tree1.get_preorder(), [10, 5, 2, 7, 30, 25])
        self.assertEqual(tree1.get_inorder(), [2, 5, 7, 10, 25, 30])

    def test_delete_case4(self):
        """After removal, the sibling of double black is red and has 0 or 2 black children"""
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 16)
        tree1.remove(18)
        self.assertEqual(tree1.get_inorder(), [1, 2, 7, 10, 15, 16, 25, 30, 40, 60, 70])
        self.assertEqual(
            tree1.get_preorder(), [16, 10, 2, 1, 7, 15, 40, 25, 30, 60, 70]
        )

    def test_delete_case5(self):
        """After removal, the sibling of double black is black and has 1 red closer child"""
        xs = [10, 5, 30, 2, 7, 25, 40, 28]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 10)
        tree1.remove(40)
        self.assertEqual(tree1.get_preorder(), [10, 5, 2, 7, 28, 25, 30])
        self.assertEqual(tree1.get_inorder(), [2, 5, 7, 10, 25, 28, 30])

    def test_delete_case6(self):
        """After removal, the sibling of double black is black and has 1 red outer child"""
        xs = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
        tree1 = generate_tree(xs)
        self.assertEqual(tree1.root.value, 16)
        tree1.remove(30)
        self.assertEqual(
            tree1.get_preorder(), [16, 10, 2, 1, 7, 15, 25, 18, 60, 40, 70]
        )
        self.assertEqual(tree1.get_inorder(), [1, 2, 7, 10, 15, 16, 18, 25, 40, 60, 70])
    
    def test_search(self):
        xs = [1,2,3,4,5,6,7,8,9,10]
        tree1 = generate_tree(xs)
        for x in xs:
            self.assertEqual(tree1.find_node_by_value(x).value, x)

if __name__ == "__main__":
    unittest.main()

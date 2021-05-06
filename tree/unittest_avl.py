# My test case is based on @Griffin's answer on Stackoverflow
# https://stackoverflow.com/a/13843966/9933734

import unittest
from functools import reduce
from typing import List
from avl import AVLNode, Empty, Inode, AVLTree


def generate_tree(elems: list[any]) -> AVLNode:
    res = AVLTree()
    for elem in elems:
        res.insert(elem)
    return res


class TestElem(unittest.TestCase):

    def test_insert_left_right_rebalance(self):
        tree1a = generate_tree([29, 4, 15])
        self.assertEqual(tree1a.root.value, 15)
        self.assertEqual(tree1a.root.left.value, 4)
        self.assertEqual(tree1a.root.right.value, 29)

        tree2a = generate_tree([21, 4, 26, 3, 9])
        tree2a.insert(15)
        self.assertEqual(tree2a.get_inorder(), [3, 4, 9, 15, 21, 26])
        self.assertEqual(tree2a.get_preorder(), [9, 4, 3, 21, 15, 26])

        tree3a = generate_tree([20, 4, 26, 3, 9, 21, 30, 2, 7, 11])
        tree3a.insert(15)
        self.assertEqual(tree3a.get_preorder(), [
                         9, 4, 3, 2, 7, 20, 11, 15, 26, 21, 30])
        self.assertEqual(tree3a.get_inorder(), [
                         2, 3, 4, 7, 9, 11, 15, 20, 21, 26, 30])

        tree3b = generate_tree([20, 4, 26, 3, 9, 21, 30, 2, 7, 11])
        tree3b.insert(8)
        self.assertEqual(tree3b.get_inorder(), [
                         2, 3, 4, 7, 8, 9, 11, 20, 21, 26, 30])
        self.assertEqual(tree3b.get_preorder(), [
                         9, 4, 3, 2, 7, 8, 20, 11, 26, 21, 30])

    def test_delete(self):
        tree1 = generate_tree([2, 1, 4, 3, 5])
        tree1.remove(1)
        self.assertEqual(tree1.get_inorder(), [2, 3, 4, 5])
        self.assertEqual(tree1.get_preorder(), [4, 2, 3, 5])

        tree3 = generate_tree([5, 2, 8, 1, 3, 7, 10, 4, 6, 9, 11, 12])
        tree3.remove(1)
        self.assertEqual(tree3.get_inorder(), [
                         2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(tree3.get_preorder(), [
                         8, 5, 3, 2, 4, 7, 6, 10, 9, 11, 12])

    def test_state_of_inserting_and_deleting(self):
        """
        tree insert method will return True if inserting is successful, False if data already existed
        tree remove method will return True if removing is successful, False if data does not exist
        """
        tree1 = generate_tree([2, 1, 4, 3, 5])
        s1 = tree1.insert(2)
        self.assertEqual(s1, False)
        s2 = tree1.insert(6)
        self.assertEqual(s2, True)
        d1 = tree1.remove(3)
        self.assertEqual(d1, True)
        d2 = tree1.remove(88)
        self.assertEqual(d2, False)


if __name__ == "__main__":
    unittest.main()

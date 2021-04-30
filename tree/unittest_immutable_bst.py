import unittest
from functools import reduce
from typing import List
from ImmutableBinarySearchTree import BST, Empty, Inode


def generate_tree(elems: [int]) -> BST:
    x = reduce(lambda res, elem: res.insert(elem), elems, Inode(elems[0]))
    return x


class TestElem(unittest.TestCase):

    def test_elements(self):
        tree1 = generate_tree(
            [10, 8, 16, 7, 9, 14, 18, 12, 15, 11, 13, 17, 19, 6])
        self.assertEqual(tree1.value, 10, "should equal")
        self.assertEqual(tree1.left.left.left.value, 6, "should equal")
        self.assertEqual(tree1.right.left.right.value, 15, "should equal")
        self.assertIsInstance(
            tree1.right.right.right.right, Empty, "should belong")

    def test_search(self):
        tree2 = generate_tree(
            [10, 8, 16, 7, 9, 14, 18, 12, 15, 11, 13, 17, 19, 6])
        self.assertEqual(tree2.search(9), ['L', 'R'], "should equal")
        self.assertEqual(tree2.search(17), ['R', 'R', 'L'],  "should equal")
        self.assertEqual(tree2.search(
            13), ['R', 'L', 'L', 'R'],  "should equal")
        self.assertEqual([], tree2.search(10.5))
        self.assertEqual([], tree2.search(5))
        self.assertEqual([], tree2.search(20))
        self.assertEqual([], tree2.search(11.5))
        self.assertEqual([], tree2.search(30))

    def test_remove(self):
        pass


if __name__ == "__main__":
    unittest.main()

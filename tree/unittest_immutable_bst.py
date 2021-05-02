import unittest
from functools import reduce
from typing import List
from ImmutableBinarySearchTree import BST, Empty, Inode


def generate_tree(elems: [int]) -> BST:
    x = reduce(lambda res, elem: res.insert(elem), elems, Inode(elems[0]))
    return x


class TestElem(unittest.TestCase):

    def test_elements(self):
        tree1 = generate_tree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(tree1.value, 5)
        self.assertEqual(tree1.left.left.value, 2)
        self.assertEqual(tree1.right.left.value, 6)
        self.assertIsInstance(
            tree1.right.right.right, Empty)
        self.assertEquals(tree1.inorder(), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(tree1.preorder(), [5, 3, 2, 4, 7, 6, 8])
        self.assertEqual(tree1.postorder(), [2, 4, 3, 6, 8, 7, 5])

    def test_remove(self):
        tree1 = generate_tree([5, 3, 7, 2, 4, 6, 8])
        tree2 = tree1.remove(5)
        self.assertEqual(tree2.inorder(), [2, 3, 4, 6, 7, 8])
        self.assertEqual(tree2.preorder(), [6, 3, 2, 4, 7, 8])
        self.assertEqual(tree2.postorder(), [2, 4, 3, 8, 7, 6])


if __name__ == "__main__":
    unittest.main()

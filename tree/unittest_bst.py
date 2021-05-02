import unittest
from functools import reduce
from typing import List
from bst import BST, TreeNode, Inode, Empty


def generate_tree(elems: [int]) -> BST:
    tree = BST()
    for elem in elems:
        tree.insert(elem)
    return tree


class TestElem(unittest.TestCase):

    def test_insert_elements(self):
        elems = [5, 3, 7, 2, 4, 6, 8]
        tree1 = generate_tree(elems)
        self.assertEqual(tree1.root.value, 5, "should equal")
        self.assertEquals(tree1.get_inorder(), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(tree1.get_preorder(), [5, 3, 2, 4, 7, 6, 8])
        self.assertEqual(tree1.get_postorder(), [2, 4, 3, 6, 8, 7, 5])

    def test_remove(self):
        elems = [5, 3, 7, 2, 4, 6, 8]
        tree1 = generate_tree(elems)
        remove_status1 = tree1.remove(5)
        self.assertTrue(remove_status1)
        self.assertEqual(tree1.get_inorder(), [2, 3, 4, 6, 7, 8])
        self.assertEqual(tree1.get_preorder(), [6, 3, 2, 4, 7, 8])
        self.assertEqual(tree1.get_postorder(), [2, 4, 3, 8, 7, 6])


if __name__ == "__main__":
    unittest.main()

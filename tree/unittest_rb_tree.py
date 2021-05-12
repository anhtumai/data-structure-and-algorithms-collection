import unittest
from red_black_tree import RBNode, Empty, Inode, RBTree


def generate_tree(elems: list[any]) -> RBTree:
    res = RBTree()
    for elem in elems:
        res.insert(elem)
    return res


class TestElem(unittest.TestCase):
    def test_insert(self):
        tree1 = generate_tree([10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70])
        print(tree1.root)


if __name__ == "__main__":
    unittest.main()

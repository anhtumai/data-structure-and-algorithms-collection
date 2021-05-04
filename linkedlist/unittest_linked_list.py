import unittest

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList


def convert_array_to_singly_linked_list(elems: list[any]) -> SinglyLinkedList:
    res = SinglyLinkedList()
    for elem in elems:
        res.insert_tail(elem)
    return res


def convert_array_to_doubly_linked_list(elems: list[any]) -> DoublyLinkedList:
    res = DoublyLinkedList()
    for elem in elems:
        res.insert_tail(elem)
    return res


class TestSinglyLinkedList(unittest.TestCase):
    def test_basic_functionality(self):
        singly_list = convert_array_to_singly_linked_list(
            [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(singly_list[3], 4)
        self.assertEqual(singly_list.get_head(), 1)
        self.assertEqual(singly_list.get_tail(), 7)
        self.assertEqual(singly_list.head.next.next.next.next.data, 5)
        self.assertEqual(singly_list[3], 4)

    def test_insert(self):
        singly_list = convert_array_to_singly_linked_list(
            [1, 2, 3, 5, 6, 7])
        singly_list.insert_nth(3, 4)
        self.assertEqual(singly_list[3], 4)
        singly_list.insert_tail(8)
        self.assertEqual(singly_list.get_tail(), 8)
        singly_list.insert_head(0)
        self.assertEqual(singly_list.get_head(), 0)
        self.assertEqual(singly_list[1], 1)

    def test_remove(self):
        singly_list = convert_array_to_singly_linked_list(
            [0, 1, 2, 3, 5, 6, 7, 8])
        singly_list.delete_head()
        singly_list.delete_tail()
        self.assertEqual(singly_list.get_head(), 1)
        self.assertEqual(singly_list.get_tail(), 7)
        singly_list.delete_nth(2)
        self.assertEqual(singly_list[2], 5)

    def test_set_item(self):
        singly_list = convert_array_to_singly_linked_list(
            [0, 1, 2, 3, 4, 5, 6, 7])
        singly_list[1] = 2
        self.assertEqual(singly_list[1], 2)
        singly_list[7] = 100
        self.assertEqual(singly_list[7], 100)

    def test_reverse(self):
        singly_list = convert_array_to_singly_linked_list(
            [0, 1, 2, 3, 4, 5, 6, 7])
        singly_list.in_place_reverse()
        self.assertEqual(singly_list.get_head(), 7)
        self.assertEqual(singly_list.get_tail(), 0)
        self.assertEqual(singly_list[2], 5)


class TestDoublyLinkedList(unittest.TestCase):
    def test_basic_functionality(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(doubly_list[3], 4)
        self.assertEqual(doubly_list.get_head(), 1)
        self.assertEqual(doubly_list.get_tail(), 7)
        self.assertEqual(doubly_list.head.next.next.next.next.data, 5)
        self.assertEqual(doubly_list[3], 4)

    def test_insert(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [1, 2, 3, 5, 6, 7])
        doubly_list.insert_nth(3, 4)
        self.assertEqual(doubly_list[3], 4)
        doubly_list.insert_tail(8)
        self.assertEqual(doubly_list.get_tail(), 8)
        doubly_list.insert_head(0)
        self.assertEqual(doubly_list.get_head(), 0)
        self.assertEqual(doubly_list[1], 1)

    def test_remove(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [0, 1, 2, 3, 5, 6, 7, 8])
        doubly_list.delete_head()
        doubly_list.delete_tail()
        self.assertEqual(doubly_list.get_head(), 1)
        self.assertEqual(doubly_list.get_tail(), 7)
        doubly_list.delete_nth(2)
        self.assertEqual(doubly_list[2], 5)

    def test_set_item(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [0, 1, 2, 3, 4, 5, 6, 7])
        doubly_list[1] = 2
        self.assertEqual(doubly_list[1], 2)
        doubly_list[7] = 100
        self.assertEqual(doubly_list[7], 100)

    def _test_double_binding(self, doubly_list: DoublyLinkedList) -> None:
        for i in range(len(doubly_list) - 1):
            node = doubly_list._get_node(i)
            self.assertEqual(node.data, node.next.prev.data)

    def test_double_binding(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [0, 1, 2, 3, 4, 5, 6, 7])
        self._test_double_binding(doubly_list)

        doubly_list.delete_head()
        doubly_list.delete_nth(3)
        doubly_list.delete_tail()
        self._test_double_binding(doubly_list)
        self.assertEqual(doubly_list._get_node(
            4).prev, doubly_list._get_node(3))
        doubly_list.insert_nth(2, 100)
        doubly_list.insert_head(10000)
        doubly_list.insert_tail(9232)
        self._test_double_binding(doubly_list)

    def test_reverse(self):
        doubly_list = convert_array_to_doubly_linked_list(
            [0, 1, 2, 3, 4, 5, 6, 7])
        doubly_list.in_place_reverse()
        self._test_double_binding(doubly_list)
        self.assertEqual(doubly_list.get_head(), 7)
        self.assertEqual(doubly_list.get_tail(), 0)
        self.assertEqual(doubly_list[2], 5)


if __name__ == "__main__":
    unittest.main()

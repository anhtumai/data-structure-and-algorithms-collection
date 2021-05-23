from singly_linked_list import SinglyLinkedList, Node


def cycle_detection(linked_list: SinglyLinkedList) -> tuple[bool, Node]:
    """
    If cycle is present, return True, and the start node of the cycle
    Else return False, None
    """
    turtoise = linked_list.head
    hare = linked_list.head

    is_started = False

    while turtoise != None and hare != None and hare.next != None:
        if (turtoise == hare and is_started):
            return True, find_start_of_cycle(linked_list, turtoise)
        is_started = True
        turtoise = turtoise.next
        hare = hare.next.next
    return False, None


def find_start_of_cycle(linked_list: SinglyLinkedList, collision_node: Node) -> Node:
    ptr1 = linked_list.head
    ptr2 = collision_node
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


def convert_array_to_singly_linked_list(elems: list[any]) -> SinglyLinkedList:
    res = SinglyLinkedList()
    for elem in elems:
        res.insert_tail(elem)
    return res


if __name__ == "__main__":
    # Create a linked list with cycle
    ll1 = convert_array_to_singly_linked_list([1, 2, 3, 4, 5, 6])
    tail_node = ll1._get_node(len(ll1)-1)
    third_node = ll1._get_node(2)
    tail_node.next = third_node

    has_cycle, start_node = cycle_detection(ll1)

    print(has_cycle, start_node.data)

    ll2 = convert_array_to_singly_linked_list([1, 2, 3, 4, 5, 6, 7])

    print(cycle_detection(ll2))

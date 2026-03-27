"""Ninth kata"""

class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):

    fake_node = Node(0)
    fake_node.next = head
    prev = fake_node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second
        prev = first


    return fake_node.next

"""Tenth kata"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("this linked list is too short")

    first_head = head
    second_head = head.next

    current_1 = first_head
    current_2 = second_head

    while current_2 and current_2.next:
        current_1.next = current_2.next
        current_1 = current_1.next

        current_2.next = current_1.next
        current_2 = current_2.next

    current_1.next =  None
    if current_2:
        current_2.next = None
    return Context(first_head, second_head)

"""Forth kata"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise ValueError("The linkedkist is empty")

    if index < 0:
        raise ValueError("n is less than 0")

    current = node
    for _ in range(index):
        current = current.next
        if current is None:
            raise ValueError("n is larger than the list")

    return current

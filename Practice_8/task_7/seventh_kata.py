"""Seventh kata"""

class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}"

def reverse(head):
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return new_head


ll = Node(1, Node(2, Node(5)))
print(reverse(ll))

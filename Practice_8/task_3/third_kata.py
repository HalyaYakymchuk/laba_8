"""Third kata"""

'''
Node is defined in preloaded like this:
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return new_node

def build_one_two_three():
    res = None
    res = push(res, 3)
    res = push(res, 2)
    res = push(res, 1)
    return res

"""Second kata"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(" -> ")

    if parts[0] == "None":
        return None

    remaining_str = " -> ".join(parts[1:])

    return Node(int(parts[0]), linked_list_from_string(remaining_str))

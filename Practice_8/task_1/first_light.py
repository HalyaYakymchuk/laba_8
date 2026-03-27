"""First kata"""

def stringify(node):
    if node is None:
        return "None"
    return f"{node.data} -> {stringify(node.next)}"

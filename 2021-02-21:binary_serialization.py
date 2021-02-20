
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """
    >>> Node("root", Node("left", Node("left.left")), Node("right"))
    "Node(root, Node(left, left.left, None), Node("right", None, None))"
    """
    if root.left and root.right:
        return 'Node("%s", %s, %s)' % (root.val, serialize(root.left), serialize(root.right))
    elif root.left:
        return 'Node("%s", %s, None)' % (root.val, serialize(root.left))
    elif root.right:
        return 'Node("%s", None, %s)' % (root.val, serialize(root.right))
    else:
        return 'Node("%s", None, None)' % (root.val)


def deserialize(s):
    """
    >>> deserialize('Node(root, Node(left, left.left, None), Node("right", None, None))')
    Node("root", Node("left", Node("left.left")), Node("right"))
    """
    return eval(s)


node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.val == "left.left"

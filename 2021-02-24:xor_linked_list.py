
class XORLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class XORLinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        """ adds element to the end
        """
        newnode = XORLinkedListNode(element)
        if self.head is None:
            self.head = newnode
            return
        curr = self.head
        while curr:
            if curr.next is None:
                break
            curr = curr.next
        curr.next = newnode

    def get(self, index):
        """ return the node at index
        """
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value


import ctypes


# This is hacky. It's a data structure for C, not python.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # This is to prevent garbage collection

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        # Without this line, Python thinks there is no way to reach nodes between
        # head and tail.
        self.__nodes.append(node)


    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value


l = XorLinkedList()
l.add(Node(3))
l.add(Node(1))
l.add(Node(12))
# solution = lambda x: ctypes.cast(id(l.get(x)), ctypes.py_object).value.val
solution = lambda x: l.get(x).val

test_cases = [
    # input, output
    (1, 1),
    (2, 12),
    (0, 3),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

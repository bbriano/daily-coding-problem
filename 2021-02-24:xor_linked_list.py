
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


l = XORLinkedList()
l.add(3)
l.add(1)
l.add(12)
solution = l.get

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

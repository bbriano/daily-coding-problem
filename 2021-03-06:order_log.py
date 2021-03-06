class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class OrderLog:
    def __init__(self):
        self.head = None

    def record(self, order_id):
        """
        adds order_id to the log
        Time: O(1)
        """
        new_order = Node(order_id)
        new_order.next = self.head
        self.head = new_order

    def get_last(self, i):
        """
        gets the ith last element from the log.
        input: i -- 1 <= i <= N
        output: a list of the last ith order ids
        Time: O(i)
        """
        ids = []
        cur = self.head
        for _ in range(i):
            ids.append(cur.val)
            cur = cur.next
        return ids


o = OrderLog()
o.record(2)
o.record(1)
o.record(4)
o.record(3)
solution = o.get_last

test_cases = [
    # input, output
    (1, [3]),
    (3, [3,4,1]),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

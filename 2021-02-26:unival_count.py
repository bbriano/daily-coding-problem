
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unival_count(root):
    return unival_count_aux(root)[1]

def unival_count_aux(cur):
    if not cur.left and not cur.right:
        return (True, 1)

    left_is_unival, left_count = unival_count_aux(cur.left) if cur.left else (True, 0)
    right_is_unival, right_count = unival_count_aux(cur.right) if cur.right else (True, 0)

    is_unival = False
    count = left_count + right_count

    if left_is_unival and right_is_unival and \
    (not cur.left or cur.left.val) == (not cur.right or cur.right.val) == cur.val:
        is_unival = True
        count += 1

    return (is_unival, count)


solution = unival_count

test_cases = [
    # input, output
    (Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))), 5),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

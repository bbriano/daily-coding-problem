

def max_sum_non_adj(lst):
    """
    Time:  O(n)
    Space: O(1)
    """
    res = lst[-1]
    i = len(lst)-2
    b, c, d = True, True, True

    while i >= 0:
        a = False
        if not b:
            res += lst[i]
            a = True
        elif lst[i] > lst[i+1]:
            res += lst[i] - lst[i+1]
            a, b = True, False
        if b == c == d == False:
            res += lst[i+2]
            c = True
        b, c, d = a, b, c
        i -= 1

    return res


solution = max_sum_non_adj

test_cases = [
    # input, output
    ([5, 2, 1, 1, 5], 11),
    ([2, 4, 6, 2, 5], 13),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

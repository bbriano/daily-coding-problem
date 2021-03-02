
def stair_count(n):
    """
    Time:  O(2^n)
    Space: O(2^n)
    """
    if n < 0:
        return 0
    elif n in {0,1}:
        return 1
    return stair_count(n-1) + stair_count(n-2)


solution = stair_count

test_cases = [
    # input, output
    (4, 5),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

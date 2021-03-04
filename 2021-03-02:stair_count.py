
def stair_count(n):
    """
    Time:  O(2^n)
    Space: O(2^n)
    """
    if n <= 1:
        return 1
    return stair_count(n-1) + stair_count(n-2)


def stair_count_v2(n):
    """
    Time:  O(n)
    Space: O(1)
    """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def stair_count_v3(n, X):
    """
    Time:  O(n * k)
    Space: O(k)
    """
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i-x] for x in X if i-x >= 0)
    return cache[n]


solution = lambda x: stair_count_v3(x, {1,2})

test_cases = [
    # input, output
    (4, 5),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

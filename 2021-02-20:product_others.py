def product_others(a):
    """
    Time: O(n)
    Space: O(n)
    """
    product = 1
    for e in a:
        product *= e
    res = a[:]
    for i in range(len(res)):
        res[i] = product // res[i]
    return res


def product_others_nodiv(lst):
    """
    Time:  O(n^2)
    Space: O(n)
    """
    res = lst[:]
    n = len(lst)
    for i in range(n):
        product = 1
        factors = [ lst[j] if i!=j else 1 for j in range(n) ]
        for f in factors:
            product *= f
        res[i] = product
    return res


def products(lst):
    """
    Time:  O(n)
    Space: O(n)

    res[i] = product( lst[:i] + lst[i+1:] )
           = product( lst[:i] ) * product( lst[i+1:] )

    left[i] = product( lst[:i] )
    right[i] = product( lst[i+1:] )
    res[i] = left[i] * right[i]
    """
    n = len(lst)

    # generate product prefix and product suffix
    left, right = [1]*n, [1]*n
    for i in range(1, n):
        left[i] = left[i-1] * lst[i-1]
        right[n-1-i] = right[n-i] * lst[n-i]  # indexing backward (n-1 to 0)

    # build result
    res = [0]*n
    for i in range(n):
        res[i] = left[i] * right[i]

    return res


solution = products

test_cases = [
    # input, output
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([3, 2, 1], [2, 3, 6]),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

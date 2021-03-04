
def length_max_substr(s, k):
    """
    Time:  O(n * k)
    Space: O( len(dict) )
    """
    c = set()
    d = dict()
    n = 0
    m = 0
    for i,e in enumerate(s):
        d[e] = i
        n += 1
        if e not in c:
            if len(c) == k:
                l = min(d, key=lambda x: d[x] if x in c else float("inf"))
                c.remove(l)
                n = i - d[l]
            c.add(e)
        m = max(m, n)
    return m


def length_max_substr_v2(s, k):
    """
    Time:  O(n * k)
    Space: O(k)
    """
    d = dict()
    n = m = 0
    for i,e in enumerate(s):
        n += 1
        if e in d:
            d[e] = i
        else:
            if len(d) == k: # d is full
                l = min(d, key=lambda x: d[x])
                n = i - d[l]
                d.pop(l)
            d[e] = i
        m = max(m, n)
    return m


solution = length_max_substr_v2

test_cases = [
    # input, output
    (("abcba", 2), 3),
    (("career expo", 3), 6),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(*inp))
    print()

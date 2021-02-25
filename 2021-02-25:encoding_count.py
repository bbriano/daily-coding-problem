

def encoding_count(inp):
    """
    111 -> { aaa,ak,ka } -> 3

    sol(12345) = sol(2345) + sol(345)
    """
    if len(inp) in [0, 1]:
        return 1
    if inp[0] == '0':
        return 0

    assert len(inp) >= 2
    assert inp[0] != '0'

    onelead = encoding_count(inp[1:])
    twolead = encoding_count(inp[2:]) if int(inp[:2]) <= 26 else 0

    return onelead + twolead


solution = encoding_count

test_cases = [
    # input, output
    ('111', 3),
    ('12212', 8),
    ('4223', 3),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()

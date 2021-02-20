def func_v1(inp):
    return inp


solution = func_v1

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

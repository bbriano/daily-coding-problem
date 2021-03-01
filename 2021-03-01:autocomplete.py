

def autocomplete(s, words):
    return list(filter(lambda w: w[:len(s)] == s, words))


solution = autocomplete

test_cases = [
    # input, output
    (("de", ["dog", "deer", "deal"]), ["deer", "deal"]),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(*inp))
    print()


def longest_dir_path(fstring):
    curmax = 0
    stack = [""]
    for chunk in fstring.split("\n"):
        d = chunk.rfind("\t") + 1
        stack = stack[:d]
        stack.append(len(chunk) - d)
        if "." in chunk:
            curmax = max(curmax, sum(stack) + len(stack) - 1)
    return curmax


test_cases = [
    # input, output
    ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
    ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", 32),
]

for inp, out in test_cases:
    got = longest_dir_path(inp)
    if got != out:
        print("input:   ", inp)
        print("expected:", out)
        print("got:     ", got)
        print()

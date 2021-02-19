

def sum_of_two(a, k):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == k:
                return True
    return False


def sum_of_two_v2(a, k):
    """
    Time: O(n)
    Space: O(n)
    """
    target = set()
    for e in a:
        target.add(k-e)
    for e in a:
        if e in target:
            return True
    return False


solution = sum_of_two_v2

a = [10, 15, 3, 7]
k = 17
print("input:   ", a, k)
print("expected:", True)
print("got:     ", solution(a, k))

print()

a = [15, 3, 7]
k = 17
print("input:   ", a, k)
print("expected:", False)
print("got:     ", solution(a, k))

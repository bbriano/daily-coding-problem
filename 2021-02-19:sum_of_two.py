

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


def sum_of_two_v3(a, k):
    """
    Time: O(n)
    Space: O(n)
    """
    target = set()
    for e in a:
        if e in target:
            return True
        target.add(k-e)
    return False


def sum_of_two_v4(a, k):
    """
    Time:  O(n * log(n))
    Space: O(1)
    """
    a.sort()
    for i in range(len(a)):
        target = k-a[i]
        if binary_search(a, target) != -1:
            return True
    return False


def binary_search(lst, e):
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return 0 if lst[0] == e else -1
    mid = len(lst) // 2
    if lst[mid] == e:
        return mid
    left_i = binary_search(lst[:mid], e)
    right_i = binary_search(lst[mid:], e)
    return (left_i != -1 and left_i) or (right_i != -1 and right_i+mid) or -1


solution = sum_of_two_v4

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

from collections import deque

def max_subarray(a, k):
    q = deque()
    q.append(0)
    for i in range(1, len(a)):
        if q[0] < i-k+1: q.popleft()
        while q and a[q[-1]] <= a[i]: q.pop()
        q.append(i)
        if i >= k-1: print(a[q[0]])

max_subarray([10,5,2,7,8,7], 3) # 10 7 8 8

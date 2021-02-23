
def missing_positive_integer(lst):
    """
    Time:  O(n^2)
    Space: O(1)
    """
    left = -1
    num = 1
    i = 0
    forward = True

    while True:
        if i >= len(lst):
            break

        if lst[i] == num:
            num += 1
            forward = False
            if left+1 == i:
                left = i
                True

        if i <= left+1:
            forward = True
            i += 1
        else:
            i = i + (1 if forward else -1)

    return num


solution = missing_positive_integer

test_cases = [
    # input, output
    ([3, 4, -1, 1], 2),
    ([1, 2, 0], 3),
    ([1, 4, 6, 3, 2, 6], 5),
    ([1, 4, 6, 3, 2, 6, 6, 4, 3, 2, 0], 5),
]

for inp, out in test_cases:
    print("input:   ", inp)
    print("expected:", out)
    print("got:     ", solution(inp))
    print()



def first_missing_positive(nums):
    if not nums:
        return 1
    for i, _ in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
            if nums[i] == nums[nums[i] - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

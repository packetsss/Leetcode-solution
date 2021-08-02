"""
Find the longest subarray that sums up to the target value

e.g.
a = [1, 2, 3, 7, 5]
s = 12

Answer: [1, 3]
"""

a = [1, 2, 3, 7, 5]
s = 12

def sliding_window_approach(a: list, s: int) -> list:
    rst = [0, 0]
    left = 0
    for right in range(len(a)):
        print(left, right)
        while sum(a[left:right]) > s:
            print(left, right)
            left += 1

        if sum(a[left:right]) == s:
            cur_rst = [left, right - 1]
            rst = cur_rst if cur_rst[1] - cur_rst[0] > rst[1] - rst[0] else rst
    return rst

print(sliding_window_approach(a, s))

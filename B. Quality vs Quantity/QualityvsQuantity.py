
# O(n) time,
# O(1) space,
# Approach: two pointers, greedy, sorting

from typing import List


def isPaintable(lst: List[int], n: int) -> None:
    lst.sort()
    l, r = 1, n-1
    blue_sum = lst[0]
    red_sum = 0
    while l < r:
        blue_sum += lst[l]
        red_sum += lst[r]
        l +=1
        r -=1
        if red_sum > blue_sum:
            print('YES')
            return

    print('NO')


t = int(input())
for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    isPaintable(seq, n)
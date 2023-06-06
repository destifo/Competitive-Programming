'''
https://codeforces.com/problemset/problem/1642/B
'''


from collections import Counter
from typing import List


def findMinStrngthSum(powers: List[int], n) -> None:
    power_types = Counter(powers)
    m = len(power_types)

    for i in range(n):
        print(max(m, i+1), end=" ")
    print()


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    findMinStrngthSum(a, n)
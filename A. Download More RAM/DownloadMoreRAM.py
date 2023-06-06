
# O(nlogn) time,
# O(n) space,
# Approach: greedy,

from typing import List


def printMaxRam(softwares: List[List[int]], k) -> None:
    softwares.sort()
    for sw in softwares:
        if sw[0] > k:   break
        k +=sw[1]

    print(k)


t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    sw = [[0, 0] for i in range(n)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        sw[i][0] = a[i]
        sw[i][1] = b[i]

    printMaxRam(sw, k)
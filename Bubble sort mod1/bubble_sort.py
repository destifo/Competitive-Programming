"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""


import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    array_length = len(a)
    swap_no = 0
    for i in range(array_length):
        for j in range(array_length - 1):
            if a[j] > a[j + 1]:
                swap_no += 1
                a[j], a[j + 1] = a[j + 1], a[j]
    print("Array is sorted in", swap_no, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    return 

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
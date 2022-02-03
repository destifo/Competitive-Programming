"""
https://www.hackerrank.com/challenges/insertionsort1/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    unsorted_num = arr[-1]
    index = -2
    while (index >= (-1 * n)) and (unsorted_num < arr[index]):
        arr[index + 1] = arr[index];
        index -=1
        print(*arr, sep = " ")
    arr[index + 1] = unsorted_num
    print(*arr, sep = " ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

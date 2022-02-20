'''
https://www.hackerrank.com/challenges/counting-valleys/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):# an Elegant Solution, wouldn't you say ;)
    # Write your code here
    valleys = 0
    height = 0
    isSealevel = True
    for dirx in path:
        if isSealevel:
            isSealevel = False
            if dirx == 'U':
                height += 1
            if dirx == 'D':
                height -= 1
                valleys += 1
            continue
        if dirx == 'U':
            height += 1
        if dirx == 'D':
            height -= 1
        if height == 0:
            isSealevel = True
    
    return valleys
        
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)
    #fptr.write(str(result) + '\n')
#
    #fptr.close()

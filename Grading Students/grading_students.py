
"""
https://www.hackerrank.com/challenges/grading/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    final_result = list()
    for grade in grades:
        if grade % 5 == 0 or grade < 38:
            final_result.append(grade)
            continue
        near_roundable_num = None
        for num in range(grade + 1, grade + 5):
            if num % 5 == 0:
                near_roundable_num = num
        if (near_roundable_num - grade) < 3:
            final_result.append(near_roundable_num)
        else:
            final_result.append(grade)
    return final_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

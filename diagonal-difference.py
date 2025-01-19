# Week 4 Hackering Questions
# Q1
# https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(arr)):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][len(arr) - 1 - i]
    return abs(diagonal1 - diagonal2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#https://www.hackerrank.com/challenges/utopian-tree/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    case_type = 1
    height = 0
    for i in range(0,n+1):
        if case_type == 1:
            height += 1
            case_type = 0
        else:
            height *= 2
            case_type = 1
    return height
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

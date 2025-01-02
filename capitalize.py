# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return_s = ""
    uppercase_true = True
    for i in s:
        if (i != " ") and not i.isnumeric() and uppercase_true :
            return_s += i.upper()
            uppercase_true = False
        elif i == " ":
            return_s += i
            uppercase_true = True
        else:
            return_s += i
            uppercase_true = False
    return return_s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# Q3
# https://www.hackerrank.com/challenges/counter-game/problem
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    move_counter = 0
    move_result = n
    power2= False
    while move_result != 1:
        move_counter += 1
        if not power2:
            power = 0
            while 2**power < move_result:
                power += 1
            if 2**power == move_result:
                power2 == True
                move_result /= 2
            else:
                move_result -= 2**(power-1) 
        else:
            move_result /=2
    return "Louise" if move_counter % 2 == 1 else "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

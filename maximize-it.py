# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

max_mod_sum = max(sum(x**2 for x in combination) % m for combination in product(*lists))

print(max_mod_sum)

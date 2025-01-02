# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    sr = ""
    for i in s:
        sr += i.upper() if i.lower()==i else i.lower() 
    return sr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

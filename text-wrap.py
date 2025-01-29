# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    start = 0
    rstr = ""
    while start + max_width < len(string)-1 :
        rstr += string[start:start + max_width]+"\n"
        start += max_width
    rstr += string[start:]        
    return rstr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
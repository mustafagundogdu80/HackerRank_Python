# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
def split_and_join(line):
    # write your code here
    rline = ""
    for i in line:
        if i == " ":
            rline += "-"
        else:
            rline +=i
    return rline
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

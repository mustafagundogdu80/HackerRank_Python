# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    counter = 0
    print_str = ""
    for i in string:
        if counter < k and i not in print_str :
            print_str += i
        counter += 1
        if counter == k:
            print(print_str)
            print_str = ""
            counter = 0
    if counter == k:
        print(print_str)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

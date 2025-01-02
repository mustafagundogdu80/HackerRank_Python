# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    consider_list = list()
    for i in range(N):
        consider_list.append(input().split())
    arr = list()
    for i in consider_list:
        if i[0] == "insert" :
            arr.insert(int(i[1]),int(i[2]))
        elif i[0] == "print" :
            print(arr)
        elif i[0] == "remove":
            arr.remove(int(i[1]))
        elif i[0] == "append":
            arr.append(int(i[1]))
        elif i[0] == "sort":
            arr.sort()
        elif i[0] == "pop":
            arr.pop()
        elif i[0] == "reverse":
            arr.reverse()

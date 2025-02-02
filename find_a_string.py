#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count = 0
    findex = 0
    continue_loop = True
    while continue_loop:
        findex = string.find(sub_string, findex)
        if findex != -1:
            count += 1
            findex += 1
        else:
            continue_loop = False
             
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
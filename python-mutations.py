# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    rstr = ""
    counter = 0
    for i in string:
        if counter == position:
            rstr += character
        else:
            rstr += i
        counter += 1
    return rstr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
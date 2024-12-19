if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_score = second_score = 0
    for i in arr:
        if i > max_score :
            second_score = max_score
            max_score = i
        elif i > second_score and i < max_score :
            second_score = i
    print(second_score)

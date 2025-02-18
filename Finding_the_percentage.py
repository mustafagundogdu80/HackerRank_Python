if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_sum = 0
    for i in student_marks[query_name]:
        score_sum += i
    avarage = f"{(score_sum/len(student_marks[query_name])):.2f}"
    print(avarage)

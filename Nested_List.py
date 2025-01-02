if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
   
    students_sorted = sorted(students, key = lambda x : x[1])
    min_score = students_sorted[0][1]
    second_score = -1000
    second_score_list = list()
    for i in students_sorted:
        if second_score < min_score < i[1] or min_score < i[1] == second_score:
            second_score_list.append(i)
            second_score = i[1]
    if len(second_score_list) > 0:
        second_score_list_sorted = sorted(second_score_list,key=lambda x: x[0])
        for i in second_score_list_sorted:
            print(i[0])

# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 4344
c = int(input())
students_rate = []
for i in range(c):
    students = list(map(int, input().split()))
    students_sum = 0
    for j in range(1, len(students)):
        students_sum += students[j]
    students_avr = students_sum / students[0]
    students_over_avr = 0
    for k in range(1, len(students)):
        if students[k] > students_avr:
            students_over_avr += 1

    students_rate.append(students_over_avr/students[0] * 100)

for i in range(c):
    print(format(students_rate[i], ".3f") + "%")

# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 1546
n = int(input())
grades = list(map(int, input().split()))
max_grade = max(grades)
new_grades_sum = 0
for i in range(n):
    new_grades_sum += grades[i] / max_grade * 100

new_average = new_grades_sum / n
print(new_average)

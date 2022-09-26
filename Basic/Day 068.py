# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 1193
x = int(input())

group = 0
last_num_of_group = 0

while last_num_of_group < x:
    last_num_of_group += group+1
    group += 1

num1 = group
num2 = 1

for i in range(last_num_of_group - x):
    num1 -= 1
    num2 += 1

if group % 2 == 0:
    child = num1
    mother = num2
else:
    child = num2
    mother = num1

print(f"{child}/{mother}")

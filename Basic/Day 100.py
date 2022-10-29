# BOJ 단계별로 풀어보기
# 12. 정렬

# 10814
import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    age, name = input().split()
    num_list.append([int(age), name])

num_list.sort(key=lambda x: (x[0]))

for i in num_list:
    print(f"{i[0]} {i[1]}")

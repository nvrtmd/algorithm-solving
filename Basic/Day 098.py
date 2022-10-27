# BOJ 단계별로 풀어보기
# 12. 정렬

# 11651
import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    a, b = map(int, input().split())
    num_list.append([a, b])

num_list.sort(key=lambda x: (x[1], x[0]))

for i in num_list:
    print(f"{i[0]} {i[1]}")

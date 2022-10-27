# BOJ 단계별로 풀어보기
# 12. 정렬

# 11650
import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    a, b = map(int, input().split())
    num_list.append([a, b])

num_list.sort(key=lambda x: (x[0], x[1]))

for i in num_list:
    print(f"{i[0]} {i[1]}")

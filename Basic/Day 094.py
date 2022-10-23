# BOJ 단계별로 풀어보기
# 12. 정렬

# 10989
import sys

n = int(sys.stdin.readline())

count_list = [0 for _ in range(10001)]
for i in range(n):
    count_list[int(sys.stdin.readline())] += 1

for i in range(len(count_list)):
    for j in range(count_list[i]):
        print(i)

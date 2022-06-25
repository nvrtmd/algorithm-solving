# BOJ 단계별로 풀어보기
# 3. for문

# 15552
import sys

input = sys.stdin.readline
t = int(input())
num_list = []
for i in range(t):
    a, b = map(int, input().split())
    num_list.append(a + b)

for i in range(t):
    print(num_list[i])

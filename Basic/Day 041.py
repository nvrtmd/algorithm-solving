# BOJ 단계별로 풀어보기
# 3. for문

# 2439
n = int(input())
for i in range(n):
    print(" " * (n-i-1) + "*" * (i + 1))

# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 2775
def sol(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1
    return sol(k, n-1) + sol(k-1, n)


t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    print(sol(k, n))

# BOJ 단계별로 풀어보기
# 10. 재귀

# 10870
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input())

print(fibonacci(n))

# BOJ 단계별로 풀어보기
# 10. 재귀

# 10872
n = int(input())


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(n))

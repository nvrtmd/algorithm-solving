# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 2839
def sol(n):
    result = 0
    a = n // 5
    b = n % 5

    if b == 0:
        return a

    if b == 1 or b == 4:
        if a - 1 < 0:
            return -1
        else:
            return (a - 1) + ((b + 5) // 3)
    elif b == 2:
        if a - 2 < 0:
            return -1
        else:
            return (a - 2) + ((b + 10) // 3)
    elif b == 3:
        return a + b // 3
    return result


n = int(input())
print(sol(n))

# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 2581
m = int(input())
n = int(input())
sosus = []


def sosu(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(m, n+1):
    if sosu(i):
        sosus.append(i)
if len(sosus) == 0:
    print(-1)
else:
    print(sum(sosus))
    print(min(sosus))

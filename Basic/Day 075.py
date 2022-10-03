# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 1978
n = int(input())
nums = list(map(int, input().split()))
result = 0


def sosu(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


for i in nums:
    if sosu(i):
        result += 1

print(result)

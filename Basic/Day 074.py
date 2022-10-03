# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 1011
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    diff = y - x
    result = 1
    while True:
        if diff <= 3:
            result = diff
            break
        if result ** 2 < diff <= result ** 2 + result:
            result *= 2
            break
        elif diff <= (result + 1) ** 2:
            result += result + 1
            break
        result += 1
    print(result)

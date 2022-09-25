# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 2292
n = int(input())
honey = 1
result = 1

while n > honey:
    honey += 6 * result
    result += 1

print(result)

# BOJ 단계별로 풀어보기
# 4. while문

1110
n = int(input())
m = n
result = 0

while True:
    if m < 10:
        m = m * 10 + m
    else:
        l = (m // 10) + (m % 10)
        if l < 10:
            m = (m % 10) * 10 + l
        else:
            m = (m % 10) * 10 + (l % 10)
    result += 1
    if m == n:
        break

print(result)

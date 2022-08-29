# BOJ 단계별로 풀어보기
# 4. while문

# 10952
result = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    result.append(a+b)

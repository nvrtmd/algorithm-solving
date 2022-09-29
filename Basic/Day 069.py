# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 2869
a, b, v = map(int, input().split())
if (v - b) % (a-b) != 0:
    result = (v - b) // (a-b) + 1
else:
    result = (v - b) // (a-b)

print(result)

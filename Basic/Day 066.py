# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 1712
a, b, c = map(int, input().split())
if c <= b:
    print(-1)
else:
    n = a // (c-b)
    if n < 0:
        print(-1)
    else:
        print(n + 1)

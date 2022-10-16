# BOJ 단계별로 풀어보기
# 11. 브루트 포스

# 2231
n = input()


def f(n):
    for i in range(int(n)):
        m = i
        for j in range(len(str(i))):
            m += int(str(i)[j])
        if str(m) == n:
            return i


if f(n):
    print(f(n))
else:
    print(0)

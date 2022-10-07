# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 4948
while True:
    n = int(input())
    if n == 0:
        break

    every_nums = [False, False] + [True] * (2 * n-1)
    primes = []
    for i in range(2, 2 * n+1):
        if every_nums[i]:
            if i > n:
                primes.append(i)
            every_nums[i] = False
            for j in range(i * 2, 2 * n+1, i):
                every_nums[j] = False
    print(len(primes))

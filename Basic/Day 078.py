# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 1929
m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 2:
        print(i)
    else:
        if sosu(i) == True:
            print(i)

# 에라토스테네스의 체
m, n = map(int, input().split())
every_nums = [False, False] + [True] * (n-1)
primes = []

if m > 2:
    for i in range(2, n+1, 2):
        every_nums[i] = False

for i in range(2, n+1):
    if every_nums[i]:
        every_nums[i] = False
        if i >= m:
            primes.append(i)
        for j in range(i * 2, n+1, i):
            every_nums[j] = False

for i in primes:
    print(i)

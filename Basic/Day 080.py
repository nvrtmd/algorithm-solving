# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 9020
t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

every_nums = [False, False] + [True] * (max(n)-1)
primes = []

for i in range(2, max(n)+1):
    if every_nums[i]:
        primes.append(i)
        every_nums[i] = False
        for j in range(i*2, max(n) + 1, i):
            every_nums[j] = False

for i in n:
    divided = i // 2
    if divided in primes:
        print(f"{divided} {divided}")
    else:
        for j in range(1, divided):
            if (divided - j) in primes and (divided + j) in primes:
                print(f"{divided - j} {divided + j}")
                break

# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 11653
n = int(input())
result = []
minimum = 2
while n > 1:
    for i in range(minimum, n + 1):
        if n % i == 0:
            result.append(i)
            minimum = i
            n = n // i
            break

for i in range(len(result)):
    print(result[i])

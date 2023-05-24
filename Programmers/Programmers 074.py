# 카펫
def solution(brown, yellow):
    divisors = []
    for i in range(1, yellow + 1):
        if i in divisors:
            break
        if yellow % i == 0:
            divisors.append(i)
            divisors.append(yellow // i)
    divisors.sort()
    for i in range(len(divisors) // 2):
        if (divisors[i] + divisors[-i - 1]) * 2 + 4 == brown:
            return [divisors[-i - 1] + 2, divisors[i]+2]

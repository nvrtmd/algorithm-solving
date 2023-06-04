# k진수에서 소수 개수 구하기
def prime_check(n):     # n이 소수인지 아닌지 판별
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


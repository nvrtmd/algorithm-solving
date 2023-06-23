# 다음 큰 숫자
def convert(n, m):
    result = ''
    while n > 0:
        n, mod = divmod(n, m)
        result += str(mod)

    return result[::-1]


def solution(n):
    target = n
    while True:
        target += 1
        if convert(n, 2).count("1") == convert(target, 2).count("1"):
            return target

# 이진 변환 반복하기 (진법 변환 함수 포함)
def convert(n, m):
    result = ''
    while n > 0:
        n, mod = divmod(n, m)
        result += str(mod)

    return result[::-1]


def solution(s):
    count = 0
    zero_count = 0

    while s != "1":
        zero_count += s.count("0")
        length = len(s) - s.count("0")
        s = convert(length, 2)
        count += 1

    return [count, zero_count]

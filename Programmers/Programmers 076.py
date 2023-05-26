# N개의 최소공배수
def gcd(a, b):
    r = 100
    while r != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    max_num = max([a, b])
    min_num = min([a, b])
    return (max_num * min_num) // gcd(max_num, min_num)


def solution(arr):
    a = arr.pop()
    b = arr.pop()
    lcm_num = lcm(a, b)

    while arr:
        num = arr.pop()
        lcm_num = lcm(num, lcm_num)
    return lcm_num

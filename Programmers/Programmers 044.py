# 3진법 뒤집기
def solution(n):
    answer = 0
    quotient = 1
    arr = []
    while quotient != 0:
        quotient = n // 3
        remainder = n % 3
        arr.append(remainder)
        n = quotient
    arr = reversed(arr)
    for idx, num in enumerate(arr):
        answer += num * 3 ** idx

    return answer


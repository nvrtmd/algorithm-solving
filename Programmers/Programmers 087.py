# 최고의 집합
def solution(n, s):
    answer = []
    if s // n == 0:
        return [-1]

    while n > 0:
        share, _ = divmod(s, n)
        answer.append(share)
        n -= 1
        s -= share

    return answer

# 하노이의 탑
def hanoi(n, start, to, via, answer):
    if n == 1:
        answer.append([start, to])
    else:
        hanoi(n - 1, start, via, to, answer)
        answer.append([start, to])
        hanoi(n - 1, via, to, start, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

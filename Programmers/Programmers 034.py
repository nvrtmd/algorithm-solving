# 내적
def solution(a, b):
    answer = 0
    for a_number, b_number in zip(a, b):
        answer += a_number * b_number
    return answer

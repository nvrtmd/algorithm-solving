# 예상 대진표
def solution(n, a, b):
    answer = 0
    sorted_arr = sorted([a, b])
    a = sorted_arr[0]
    b = sorted_arr[1]

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer

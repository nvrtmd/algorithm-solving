# 덧칠하기
def solution(n, m, section):
    answer = 0
    pointer = 0
    for i in section:
        if pointer < i:
            pointer = i + m - 1
            answer += 1

    return answer


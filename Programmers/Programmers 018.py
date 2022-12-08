# 사탕 담기
from itertools import combinations


def solution(m, weights):
    answer = 0

    # 1부터 weights의 길이만큼 순회
    for i in range(1, len(weights) + 1):
        # weights 배열 내 요소를 i개만큼 선택
        weights_combinations = list(combinations(weights, i))

        # weights_combinations를 순회
        for combination in weights_combinations:

            # combination의 합이 m일 경우 answer에 1을 더함
            if sum(combination) == m:
                answer += 1

    return answer

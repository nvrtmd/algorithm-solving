# 피로도
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons, len(dungeons)))

    for case in cases:
        health = k
        visit_count = 0
        for i in case:
            minimum, exhausted = i
            if minimum <= health:
                health -= exhausted
                visit_count += 1
        answer = max(answer, visit_count)

    return answer

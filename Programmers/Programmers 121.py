# 기능개발 (복습)
import math


def solution(progresses, speeds):
    answer = []

    minimum_left_day = 0
    for progress, speed in zip(progresses, speeds):
        left_day = math.ceil((100 - progress) / speed)

        if minimum_left_day < left_day:
            answer.append(1)
            minimum_left_day = left_day
        else:
            answer[-1] += 1

    return answer


print(solution([93, 30, 55], [1, 30, 5]))

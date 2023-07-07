# 구명보트
from collections import deque


def solution(people, limit):
    answer = 0
    people = sorted(people)

    people_deq = deque(people)

    while people_deq:
        if len(people_deq) <= 1:
            people_deq.pop()
            answer += 1
            break
        if people_deq[0] + people_deq[-1] <= limit:
            people_deq.popleft()
        people_deq.pop()
        answer += 1

    return answer

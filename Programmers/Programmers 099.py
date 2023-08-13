# 야근 지수
import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0
    works_arr = []
    for work in works:
        heapq.heappush(works_arr, [-work, work])
    while n:
        max_work = heapq.heappop(works_arr)[1]
        max_work -= 1
        heapq.heappush(works_arr, [-max_work, max_work])
        n -= 1
    for work in works_arr:
        answer += work[1] ** 2
    return answer

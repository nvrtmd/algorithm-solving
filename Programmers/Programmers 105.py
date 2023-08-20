# 단속카메라
import heapq


def solution(routes):
    answer = 0
    routes_heap = []
    max_end_time = -30001
    for route in routes:
        heapq.heappush(routes_heap, [route[1], route[0]])

    for _ in range(len(routes)):
        end, enter = heapq.heappop(routes_heap)
        if max_end_time < enter:
            max_end_time = end
            answer += 1
    return answer

# 최소직사각형
import heapq


def solution(sizes):
    arr = []

    for size in sizes:
        h, v = size
        heapq.heappush(arr, [-max(h, v), min(h, v)])
    h, v = heapq.heappop(arr)
    max_hor = abs(h)
    max_ver = v
    for i in range(len(arr)):
        _, ver = heapq.heappop(arr)
        max_ver = max(max_ver, ver)
    return max_hor * max_ver

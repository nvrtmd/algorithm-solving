# 숫자 게임
import heapq


def solution(A, B):
    answer = 0
    a_heap = []
    b_heap = []
    for i, j in zip(A, B):
        heapq.heappush(a_heap, i)
        heapq.heappush(b_heap, j)

    if a_heap[0] > b_heap[-1]:
        return 0

    while b_heap and a_heap:
        if b_heap[0] > a_heap[0]:
            answer += 1
            heapq.heappop(a_heap)
        heapq.heappop(b_heap)

    return answer


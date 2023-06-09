# 최솟값 만들기
import heapq


def solution(A, B):
    answer = 0
    dic = {'A': sorted(A), 'B': sorted(B)}
    arr = []
    for a in A:
        heapq.heappush(arr, [a, 'B'])
    for b in B:
        heapq.heappush(arr, [b, 'A'])

    for _ in range(len(arr) // 2):
        num1, key = heapq.heappop(arr)
        num2 = dic[key].pop()
        answer += num1 * num2

    return answer

# 배상 비용 최소화
import heapq


def solution(n, works):
    # 만약 작업량의 합이 일할 수 있는 시간 n보다 작을 경우
    # 즉, 모든 일을 일할 수 있는 시간 내에 끝낼 수 있다면
    # 0을 return
    if n >= sum(works):
        return 0

    works_heap = []
    answer = 0

    # 작업량을 heap에 내림차순으로 삽입
    # 더 많은 작업량을 우선적으로 처리하기 위함
    for work in works:
        heapq.heappush(works_heap, (-work, work))

    # n이 다 소진될 때까지 반복
    while n > 0:
        # 가장 많이 남은 작업의 작업량을 꺼내서 1을 빼고
        # n에서도 1을 빼기 = 1시간을 소모하여 해당 작업 수행함
        n -= 1
        work = heapq.heappop(works_heap)[1] - 1

        # 1을 빼준 해당 작업을 다시 내림차순으로 heap에 삽입
        heapq.heappush(works_heap, (-work, work))

    # heap에 남은 작업량들을 제곱하여 answer에 할당
    for work in works_heap:
        answer += work[1] ** 2

    return answer

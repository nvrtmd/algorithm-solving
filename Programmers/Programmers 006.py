# 더 맵게
import heapq


def solution(scoville, K):
    # 스코빌 지수를 담을 heap 선언 후 초기화
    scoville_heap = []
    # 섞어야 하는 최소 횟수를 담을 변수 선언 후 초기화
    answer = 0

    # 스코빌 지수가 담긴 배열을 순회하며 heap에 추가
    # heap에서 스코빌 지수가 오름차순으로 정렬 됨
    for value in scoville:
        heapq.heappush(scoville_heap, value)

    # 가장 작은 스코빌 지수가 K보다 작은 경우 반복
    # 즉, K보다 크지 않은 요소가 존재하는 경우에 계속 반복
    while scoville_heap[0] < K:
        # 만약 스코빌 지수 heap에 남은 요소의 개수가 2개보다 적을 때
        # 즉, 더 이상 섞지 못하고 남은 1개의 요소가 K보다 작은 경우
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        # -1을 return
        if len(scoville_heap) < 2:
            return -1

        # 가장 작은 스코빌 지수와 그 다음으로 작은 스코빌 지수를 꺼내어 변수에 할당
        least_scoville = heapq.heappop(scoville_heap)
        second_least_scoville = heapq.heappop(scoville_heap)

        # 두 음식을 섞어서 만든 스코빌 지수를 다시 스코빌 지수 heap에 삽입
        heapq.heappush(scoville_heap, least_scoville +
                       second_least_scoville * 2)

        # 섞은 횟수를 1 증가시킴
        answer += 1

    return answer

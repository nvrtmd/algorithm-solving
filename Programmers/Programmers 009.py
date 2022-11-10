# 게임아이템
import heapq
from collections import deque as queue


def solution(healths, items):
    answer = []
    # 체력이 낮은 캐릭터부터 아이템을 견주어볼 것이므로
    # 캐릭터의 체력을 오름차순으로 정렬
    healths.sort()

    items_index_heap = []

    # 아이템 배열을 순회하며 아이템 별 (감소되는 체력, 공격력, 해당 아이템의 인덱스) 튜플을
    # items_with_index 큐에 삽입
    items_with_index = queue(sorted([(reduced_health, attack, index)
                             for index, (attack, reduced_health) in enumerate(items)]))

    # 캐릭터 체력을 순서대로 순회
    for health in healths:
        # items_with_index 큐에 요소가 남지 않을 때까지 반복
        while items_with_index:
            # items_with_index 큐의 가장 처음 요소(감소되는 체력 양이 가장 작은 아이템)를
            # reduced_health에 할당
            reduced_health = items_with_index[0][0]

            # 선택된 캐릭터의 체력 health에서 reduced_health을 뺀 값이 100보다 작으면
            # break로 while문 탈출하여 if items_index_heap:으로 이동
            if health - reduced_health < 100:
                break

            # 선택된 캐릭터의 체력 health에서 reduced_health을 뺀 값이 100보다 크거나 같으면
            # 해당 아이템을 큐에서 pop
            _, attack, index = items_with_index.popleft()

            # 캐릭터가 장착할 수 있는 아이템들(items_index_heap) 중 공격력이 가장 높은 것을 장착시켜야 하므로
            # 공격력 기준 내림차순으로 index에 1을 더한 값을 heap에 삽입
            heapq.heappush(items_index_heap, (-attack, index + 1))

        # break로 while문을 탈출했을 경우
        # 만약 items_index_heap에 요소가 있을 경우
        # 즉, 캐릭터가 장착할 수 있는 아이템이 있는 경우
        if items_index_heap:
            # 가장 첫번째 요소, 즉, 그 중 가장 공격력이 높은 아이템의 index를 answer에 추가
            answer.append(heapq.heappop(items_index_heap)[1])

    return sorted(answer)

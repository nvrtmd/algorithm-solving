# 두 큐 합 같게 만들기
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_of_queue1 = sum(queue1)
    sum_of_queue2 = sum(queue2)

    for _ in range((len(queue1)-1)*3+1):
        if sum_of_queue1 == sum_of_queue2:
            return answer
        elif sum_of_queue1 > sum_of_queue2:
            popped_number = queue1.popleft()
            queue2.append(popped_number)
            sum_of_queue1 -= popped_number
            sum_of_queue2 += popped_number
        else:
            popped_number = queue2.popleft()
            queue1.append(popped_number)
            sum_of_queue2 -= popped_number
            sum_of_queue1 += popped_number
        answer += 1

    return -1

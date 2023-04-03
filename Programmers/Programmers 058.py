# 이중우선순위큐
import heapq


def solution(operations):
    heap = []
    max_heap = []
    for operation in operations:
        task, number = operation.split(' ')
        if task == 'I':
            heapq.heappush(heap, int(number))
            heapq.heappush(max_heap, (-int(number), int(number)))
        else:
            if len(heap) == 0:
                pass
            elif number == '-1':
                minimum = heapq.heappop(heap)
                max_heap.remove((-minimum, minimum))
            elif number == '1':
                maximum = heapq.heappop(max_heap)[1]
                heap.remove(maximum)

    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]

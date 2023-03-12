# 가장 먼 노드
from collections import deque


def solution(n, edges):
    answer = 0
    counts = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    counts[1] = 1
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if counts[next_node] == 0:
                queue.append(next_node)
                counts[next_node] = counts[node] + 1

    max_count = max(counts)
    for count in counts:
        if count == max_count:
            answer += 1
    return answer

# 네트워크
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(num):
        queue = deque()
        queue.append(num)
        while queue:
            a = queue.popleft()
            visited[a] = True
            for b in range(n):
                if not visited[b] and computers[a][b]:
                    queue.append(b)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer

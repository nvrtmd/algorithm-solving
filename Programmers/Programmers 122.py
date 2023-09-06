# FloodFill (복습)
import sys
sys.setrecursionlimit(100000)


def solution(n, m, image):
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y, cur_image):
        if x < 0 or y < 0 or x >= n or y >= m:
            return

        if visited[x][y]:
            return

        if image[x][y] != cur_image:
            return
        visited[x][y] = True
        dfs(x - 1, y, image[x][y])
        dfs(x, y - 1, image[x][y])
        dfs(x + 1, y, image[x][y])
        dfs(x, y + 1, image[x][y])

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            dfs(i, j, image[i][j])
            answer += 1

    return answer


print(solution(2, 3, [[1, 2, 3], [3, 2, 1]]))
print(solution(3, 2, [[1, 2], [1, 2], [4, 5]]))

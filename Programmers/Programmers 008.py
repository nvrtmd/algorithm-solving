# FloodFill
# 프로그래머스의 최대 재귀 깊이를 늘려주기 위함
import sys
sys.setrecursionlimit(100000)


def solution(n, m, image):
    result = 0

    # 방문한 좌표를 체크하기 위한 리스트를 선언 후 모든 요소를 False로 초기화
    visited = [[False for _ in range(m)] for _ in range(n)]

    # dfs를 위한 함수 선언
    def dfs(x, y, cur_area):
        # 만약 x와 y가 0보다 작거나 각각 n, m 이상이면
        # 주어진 범위를 벗어난 좌표이므로 return
        if x < 0 or x >= n or y < 0 or y >= m:
            return

        # 만약 해당 x, y 좌표가 이미 방문 처리된 좌표라면 return
        if visited[x][y]:
            return

        # 만약 함수 호출할 때 '인자로 전달했던 칸의 값(cur_area)'와
        # 인자의 x, y좌표의 칸의 숫자 값이 다를 경우
        # 즉, 직전에 방문한 칸의 숫자 값과 현재 칸의 값이 다른 경우
        # dfs 함수를 더 호출하지 말고 return
        if image[x][y] != cur_area:
            return

        # 현재 칸의 좌표를 방문 처리
        visited[x][y] = True

        # 해당 좌표의 상하좌우 칸을 방문하는 dfs 함수 호출
        # 호출 시 상하좌우 칸의 숫자 값과 비교할 수 있게
        # cur_area에 현재 칸의 숫자 값을 전달
        dfs(x - 1, y, image[x][y])
        dfs(x, y - 1, image[x][y])
        dfs(x + 1, y, image[x][y])
        dfs(x, y + 1, image[x][y])

    # 배열 내 모든 요소를 순회하기 위한 반복문
    for i in range(n):
        for j in range(m):
            # 만약 i, j 좌표가 이미 방문 처리 되었을 경우 continue
            if visited[i][j]:
                continue

            # i, j 좌표로 dfs 함수 실행
            # 같은 숫자 값이 연속해서 배치된 경우 바로 return되지 않고
            # 같은 숫자 값이 들어간 칸 모두를 순회 후 return하기 때문에
            # 해당 숫자 값의 칸 전부가 방문 처리된 후 result에 1을 더하게 됨
            # 즉, 같은 숫자 값의 칸은 하나의 덩어리로 카운트 됨
            dfs(i, j, image[i][j])
            result += 1

    return result

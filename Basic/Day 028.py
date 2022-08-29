# n*m 크기의 얼음틀에 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫린 부분끼리 상하좌우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 얼읔틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라.


# ------------------------------------------------------


def sol(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        sol(x-1, y)
        sol(x, y+1)
        sol(x+1, y)
        sol(x, y-1)
        return True
    return False


n, m = map(int, input().split())
answer = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


for i in range(n):
    for j in range(m):
        if sol(i, j):
            answer += 1


print(answer)

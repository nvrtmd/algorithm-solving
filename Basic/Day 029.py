# n*m 크기의 직사각형 형태의 미로에서 이동할 수 있는 칸은 0으로, 이동할 수 없는 칸은 1로 표시되어있다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
# 시작 위치는 (1,1)이다. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함하여 계산한다.


# ------------------------------------------------------


from collections import deque


def sol(row, column):
    queue = deque()
    queue.append((row, column))

    while queue:
        row, column = queue.popleft()

        for i in range(4):
            new_row = row + moves[i][0]
            new_column = column + moves[i][1]

            if new_row < 0 or new_row >= num_of_row or new_column < 0 or new_column >= num_of_column:
                continue

            if graph[new_row][new_column] == 0:
                continue

            if graph[new_row][new_column] == 1:
                graph[new_row][new_column] = graph[row][column] + 1
                queue.append((new_row, new_column))

    return graph[num_of_row-1][num_of_column-1]


num_of_row, num_of_column = map(int, input().split())

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
graph = []

for i in range(num_of_row):
    graph.append(list(map(int, input())))

print(sol(0, 0))

# 여행가 A는 N*N 크기의 정사각형 공간 위에 서있다. 이 공간은 1*1 크기의 정사각형으로 나뉘어져있다.
# 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)이다.
# 여행가 A는 상하좌우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
# 여행가 A가 이동할 계획이 적힌 계획서가 놓여있으며 L은 왼쪽으로, R은 오른쪽으로, U는 위로, D는 아래로 한 칸 이동을 의미한다.
# 이 때, A가 n*N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# A가 최종적으로 도착할 지점의 좌표 X,Y를 구하라


# ------------------------------------------------------


def sol(map_scale, moves):

    position = [1, 1]
    directions = {'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1]}

    for move in moves:
        for i in range(2):
            temp = position[i] + directions[move][i]
            if temp > 0 and temp <= map_scale:
                position[i] = temp
    return position


map_scale = int(input())
moves = list(input().split())

print(sol(map_scale, moves))

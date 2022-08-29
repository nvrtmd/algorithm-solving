# 8*8 좌표평면의 특정한 한 칸에 나이트가 있다.
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하라.


# ------------------------------------------------------


# 나의 풀이

n = input()

x = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g']

moves = [[-1, 2], [1, 2], [2, 1], [2, -1],
         [1, -2], [-1, -2], [-1, -2], [-2, -1], [-2, 1]]

original_position = [x.index(n[0]), int(n[1])]
current_position = []
answer = 0

for move in moves:
    for i in range(2):
        current_position.append(original_position[i] + move[i])

    if current_position[0] > 0 and current_position[1] > 0:
        answer += 1

    current_position.clear()

print(answer)


# 수정 풀이

n = input()
x = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g']
moves = [[-1, 2], [1, 2], [2, 1], [2, -1],
         [1, -2], [-1, -2], [-1, -2], [-2, -1], [-2, 1]]
original_x = x.index(n[0])
original_y = int(n[1])
answer = 0
for move in moves:
    current_x = original_x + move[0]
    current_y = original_y + move[1]
    if current_x > 0 and current_x <= 8 and current_y > 0 and current_y <= 8:
        answer += 1

print(answer)

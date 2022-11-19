# 나머지 한 점
def solution(v):
    answer = []
    # 좌표를 x, y로 나눠서 넣을 배열 선언
    coordinates_stack = [[], []]

    # v에 담긴 좌표 배열 순회
    for coordinate in v:
        for i in range(2):
            # 만약 좌표의 x좌표와 y좌표가
            # coordinates_stack의 첫 번째, 두 번째 배열에 각각 들어있지 않다면
            # 해당 좌표의 배열에 append
            # (x좌표는 coordinates_stack의 첫 번째 배열에, y좌표는 두 번째 배열에 append)
            if coordinate[i] not in coordinates_stack[i]:
                coordinates_stack[i].append(coordinate[i])

            # 이미 들어가 있다면 해당 좌표를 배열에서 제거
            else:
                coordinates_stack[i].remove(coordinate[i])

    # coordinates_stack에 남아있는 좌표값을 하나의 리스트로 병합
    for i in range(2):
        answer.append(coordinates_stack[i][0])
    return answer

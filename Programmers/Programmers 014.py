# 방문 길이
def solution(dirs):
    # 상하좌우로 이동하기 위한 dictionary 생성
    directions_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    # 현재 x좌표와 y좌표를 담을 변수 선언 후 0으로 초기화
    current_x = 0
    current_y = 0

    # 좌표 이동 기록을 위한 set 선언
    coordinates_record = set()

    for direction in dirs:
        # 다음 x, y좌표를 next_x, next_y에 삽입
        next_x, next_y = current_x + directions_dict[direction][0], current_y + \
            directions_dict[direction][1]

        # 만약 다음 x, y좌표가 범위 안에 위치한다면
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            # coordinates_record set에 (현재 좌표, 다음 좌표), (다음 좌표, 현재 좌표)를 삽입
            # 이동 위치가 아닌 경로를 이용해야 하므로 (현재 좌표, 다음 좌표), (다음 좌표, 현재 좌표) 둘 다를 삽입해야 함
            coordinates_record.add((current_x, current_y, next_x, next_y))
            coordinates_record.add((next_x, next_y, current_x, current_y))

            # 현재 좌표를 next_x, next_y로 설정
            current_x, current_y = next_x, next_y

    # (현재 좌표, 다음 좌표), (다음 좌표, 현재 좌표)를 삽입하므로 2로 나눠줘야 함
    return len(coordinates_record) // 2

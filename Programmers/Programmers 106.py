# 방문 길이
def solution(dirs):
    x_dir = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
    y_dir = {'U': 1, 'D': -1, 'R': 0, 'L': 0}

    move_record = set()

    cur_x, cur_y = [0, 0]

    for dir in dirs:
        next_x = cur_x + x_dir[dir]
        next_y = cur_y + y_dir[dir]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            move_record.add((cur_x, cur_y, next_x, next_y))
            move_record.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = [next_x, next_y]

    return len(move_record) // 2

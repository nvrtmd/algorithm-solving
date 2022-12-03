# 자물쇠와 열쇠
def rotate_90(coordinates, size):
    rotated_coordinates = []
    for coordinate in coordinates:
        rotated_coordinates.append([coordinate[1], size - 1 - coordinate[0]])
    return rotated_coordinates


def fitting_checker(key_coordinates, lock_coordinates):
    move_coordinates = []
    for lock in lock_coordinates:
        for key in key_coordinates:
            x_distance, y_distance = [
                lock[0] - key[0], lock[1] - key[1]]
            if x_distance == y_distance:
                if len(move_coordinates) > 0 and [x_distance, y_distance] not in move_coordinates:
                    break
                else:
                    move_coordinates.append([x_distance, y_distance])

    if len(move_coordinates) == len(lock_coordinates):
        return True
    else:
        return False


def solution(key, lock):
    answer = False
    key_coordinates = []
    lock_coordinates = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_coordinates.append([i, j])

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_coordinates.append([i, j])

    for i in range(4):
        if fitting_checker(key_coordinates, lock_coordinates):
            return True
        else:
            key_coordinates = rotate_90(key_coordinates, len(key))
    return answer

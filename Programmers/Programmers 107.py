# 숫자 짝꿍
def solution(X, Y):
    answer = ''
    x = sorted(X)
    y = sorted(Y)

    x_idx = 0
    y_idx = 0

    while True:
        if x_idx >= len(x) or y_idx >= len(y):
            break
        cur_x = x[x_idx]
        cur_y = y[y_idx]

        if cur_x > cur_y:
            y_idx += 1
            continue
        elif cur_x < cur_y:
            x_idx += 1
            continue
        else:
            answer += cur_x
            x_idx += 1
            y_idx += 1

    if len(answer) <= 0:
        return '-1'

    if answer[-1] == '0':
        return '0'
    else:
        return answer[::-1]

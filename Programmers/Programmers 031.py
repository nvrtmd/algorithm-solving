# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    dolls_stack = []
    for _ in range(len(moves)):
        pick_up_position = moves.pop(0) - 1
        for i in range(len(board)):
            if board[i][pick_up_position] != 0:
                if dolls_stack:
                    if dolls_stack[-1] != board[i][pick_up_position]:
                        dolls_stack.append(board[i][pick_up_position])
                    else:
                        dolls_stack.pop()
                        answer += 2
                else:
                    dolls_stack.append(board[i][pick_up_position])

                board[i][pick_up_position] = 0
                break

    return answer

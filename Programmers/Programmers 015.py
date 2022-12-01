# 빙고
def solution(board, nums):
    answer = 0

    # 체크할 번호들을 set으로 생성
    numbers = set(nums)
    board_size = len(board)

    # 보드의 크기만큼 0으로 채워진 배열 2개 생성
    # 배열 내 요소들은 각각 해당 인덱스의 행, 열별로 체크된 칸의 개수를 나타냄
    # ex. row_line[2] = 3 이면 3번 째 행의 체크된 칸의 개수가 총 3개
    row_line = [0] * board_size
    column_line = [0] * board_size

    # 두 개의 대각선 내에 위치한 칸에 대한 개수 체크
    right_diagonal_line = 0
    left_diagonal_line = 0

    for row in range(board_size):
        for column in range(board_size):
            # 만약 해당 칸의 숫자가 numbers 내에 존재하면
            if board[row][column] in numbers:
                # 행과 열 배열(row_line, column_line) 내 해당 칸의 행과 열에 해당하는 인덱스의 값을 1 더함
                row_line[row] += 1
                column_line[column] += 1

                # 만약 해당 칸의 행과 열 숫자가 같으면 좌측 하단을 향한 대각선 내의 칸이므로
                # right_diagonal_line에 1을 더함
                if row == column:
                    right_diagonal_line += 1

                # 해당 칸의 행과 열 숫자의 합이 board_size - 1인 경우
                # 우측 하단을 향한 대각선 내의 칸이므로 left_diagonal_line에 1을 더함
                if row + column == board_size - 1:
                    left_diagonal_line += 1

    # 대각선 변수를 board_size로 나눈 나머지(각각 0 또는 1)를 answer에 더함
    answer = right_diagonal_line // board_size + left_diagonal_line // board_size

    # 행과 열 배열(row_line, column_line)의 요소를 각각 순회하며 해당 요소가 board_sized이면
    # 해당 행 또는 열 내의 모든 칸들이 체크되었다는 뜻이므로 answer 변수에 1씩 더함
    answer += sum([1 for i in range(board_size) if row_line[i] == board_size])
    answer += sum([1 for i in range(board_size)
                  if column_line[i] == board_size])
    return answer

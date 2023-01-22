# 등굣길
def solution(m, n, puddles):
    # 경우의 수를 저장할 리스트 생성
    # m개의 칸이 n행 존재
    road_map = [[0 for _ in range(m)] for _ in range(n)]
    # (0, 0) 칸의 값은 1로 설정(초기값)
    road_map[0][0] = 1

    # m개의 칸이 n행 존재하므로
    for i in range(n):
        for j in range(m):
            # 만약 i와 j가 0이면 continue ((0, 0) 칸이므로)
            if i == 0 and j == 0:
                continue

            # 만약 (j + 1, i + 1) 칸이 물에 잠긴 경우
            # (puddles는 시작 좌표가(1, 1)일 때의 좌표이므로 i와 j에 1씩 더해줘야 함)
            if [j + 1, i + 1] in puddles:
                # (i, j) 칸의 수를 0으로 설정
                # 해당 좌표는 방문할 수 없으므로
                # 방문하는 경우의 수가 0임
                road_map[i][j] = 0

            # 물에 잠기지 않은 칸의 경우
            else:
                # 해당 칸에 방문할 수 있는 경우의 수는
                # (i - 1, j) 칸과 (i, j - 1) 칸에 방문할 수 있는
                # 각각의 경우의 수의 합
                road_map[i][j] = (road_map[i - 1][j] +
                                  road_map[i][j - 1]) % 1000000007

    # (0, 0)부터 (n - 1, m - 1) 칸까지 경우의 수를 구했으므로
    return road_map[n - 1][m - 1]

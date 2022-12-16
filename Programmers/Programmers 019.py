# 주사위 게임
from itertools import product


def solution(monster, S1, S2, S3):
    monster_visit = 0

    # 주사위가 나올 수 있는 가짓수를 list로 생성
    dices_combinations = list(
        product(range(1, S1 + 1), range(1, S2 + 1), range(1, S3 + 1)))

    # 주사위 던졌을 때 나올 수 있는 모든 가짓수의 수를 visit에 할당
    visit = len(dices_combinations)

    # 주사위로 갈 수 있는 모든 칸에 대해
    # monster 배열 내에 해당 요소(해당 칸)가 존재하는지 확인
    # 즉, 주사위를 던져서 나올 수 있는 수로 몬스터가 있는 칸에 갈 수 있는 경우의 수를 측정
    for combination in dices_combinations:
        if 1 + sum(combination) in monster:
            monster_visit += 1

    return int((visit - monster_visit) / visit * 1000)

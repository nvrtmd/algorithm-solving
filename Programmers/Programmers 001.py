# 완주하지 못한 선수
from collections import Counter


def solution(participant, completion):
    answer = ''
    # Counter 모듈을 사용하여 참가자명: 참가자수 쌍으로 이뤄진 딕셔너리 생성
    part_dict = Counter(participant)

    # 완주한 사람들 리스트 순회하며 part_dict에서 해당 참가자명의 value(참가자수)의 수를 1씩 줄여나감
    for comp in completion:
        part_dict[comp] -= 1

    for part, num in part_dict.items():
        if num > 0:
            answer = part

    return answer

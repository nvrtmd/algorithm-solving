# 운송 트럭


def solution(max_weight, specs, names):
    answer = 0
    specs_dict = {}
    weight = 0

    # 물건 이름과 무게를 dictionary로 생성
    specs_dict = dict(specs)

    # names 배열 순회
    for name in names:
        # specs_dict에서 name에 해당하는 무게를 weight에 추가
        weight += int(specs_dict[name])

        # 만약 무게들의 합이 max_weight를 초과하면
        if weight > max_weight:
            # 트럭 대수에 1을 추가
            answer += 1

            # weight를 name에 해당하는 무게로 초기화
            weight = int(specs_dict[name])

    # 반복문에서 빠져나온 뒤 마지막 물건의 트럭 대수 1을 추가
    answer += 1
    return answer

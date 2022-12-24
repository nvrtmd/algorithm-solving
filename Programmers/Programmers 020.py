# 카펫
from itertools import combinations


def solution(brown, red):
    divisors = []

    # 빨간 블럭 개수의 약수들을 구한 뒤,
    # 빨간 블럭 약수들 중 두 개를 선택하여 두 수를 곱했을 때
    # 그 값이 빨간 블럭의 개수에 해당하면
    # 그 두 개의 약수의 합에 2를 곱한 뒤 4(위아래 네 개의 모서리 블럭)을 더해 봄
    # 그 값이 갈색 블럭의 개수에 해당하는지 확인한 뒤 해당하면
    # 두 약수의 곱이 빨간 블럭의 개수이며
    # 그 두 개의 약수의 합에 2를 곱한 뒤 4(위아래 네 개의 모서리 블럭)을 더한 값이
    # 갈색 블럭의 개수임

    # 빨간 블럭 개수의 약수를 구하여 divisors 리스트에 추가
    for i in range(1, red + 1):
        if red % i == 0:
            divisors.append(i)

    # 약수들을 2개씩 쌍으로 곱해봐야 하므로
    # 만약 약수들의 개수가 홀수이면 가운데값에 해당하는 약수를
    # 약수 리스트에 한번 더 추가
    if len(divisors) % 2 != 0:
        divisors.append(divisors[len(divisors) // 2])

    # 약수 리스트에서 2개를 뽑은 모든 조합 리스트 생성
    divisors_combinations = list(combinations(divisors, 2))

    # 조합 리스트에서 조합 순회
    for combination in divisors_combinations:
        # 두 약수를 곱한 값이 빨간 블럭의 개수에 해당하며 두 약수를 더한 뒤 2를 곱하고 4를 더한 값이 갈색 블럭의 개수에 해당하면
        # 해당 약수 값들을 사용하여 카펫 가로 세로의 값을 return
        if combination[0] * combination[1] == red and (combination[0] + combination[1]) * 2 + 4 == brown:
            return [max([combination[0], combination[1]]) + 2, min([combination[0], combination[1]]) + 2]

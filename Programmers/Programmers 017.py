# 세 소수의 합
from itertools import combinations


def get_primes(num):
    # 에라토스테네스의 체
    # 소수를 걸러내기 위한 boolean list
    # 0과 1은 소수가 아니므로 False로 미리 설정
    # 2부터 num까지 해당하는 인덱스는 모두 기본값 True로 설정
    primes = [False, False] + [True] * (num - 1)

    # 2부터 num의 절반에 해당하는 수까지 순회
    # 절반까지만 순회하는 이유는 i에 2를 곱한 수부터 순회할 것이므로
    for i in range(2, num // 2 + 1):
        # 만약 primes[i]가 True라면
        # 즉, i가 아직 순회를 돌지 않은 수이거나,
        # 다른 수의 배수여서 False로 변경되지 않은 경우 (= 소수의 가능성 존재)
        if primes[i]:

            # i의 2배수부터 num까지 i 간격으로 순회
            # 즉, i의 배수를 모두 탐색
            for j in range(i * 2, num, i):
                # i의 배수이면 곧 j는 i를 약수로 가지므로 소수가 될 수 없음
                # 따라서 primes[j]를 False로 설정
                primes[j] = False

    # primes[i]가 True인 i들(= 소수들)로 이뤄진 리스트를 return
    return [i for i in range(num) if primes[i]]


def solution(n):
    # n보다 작은 소수들의 리스트를 primes_list로 할당
    primes_list = get_primes(n)

    # primes_list에서 요소 3개를 뽑은 list를 n_primes에 할당
    n_primes = list(combinations(primes_list, 3))

    # n_primes 순회하며 뽑힌 3개의 요소 리스트의 총합이 n인 경우 list에 1을 추가
    # 모든 1의 총합을 return
    return sum([1 for primes in n_primes if sum(primes) == n])

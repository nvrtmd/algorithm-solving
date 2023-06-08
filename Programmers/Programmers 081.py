# 소수 찾기
from itertools import permutations
import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        b = list(permutations(list(numbers), i))
        for j in list(set(b)):
            if is_prime(int("".join(j))):
                answer.add(int("".join(j)))
    print(sorted(list(answer)))
    return len(answer)

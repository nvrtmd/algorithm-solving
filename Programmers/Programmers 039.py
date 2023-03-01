# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for number in course:
        arr = []
        for order in orders:
            arr += combinations(sorted(order), number)

        count = Counter(arr)
        if count:
            max_count = max(list(count.values()))
            if max_count >= 2:
                for key, value in count.items():
                    if count[key] == max_count:
                        answer.append(''.join(key))

    return sorted(answer)

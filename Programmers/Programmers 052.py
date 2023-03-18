# 위장
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    for i in clothes_dict.values():
        answer *= i + 1

    return answer - 1


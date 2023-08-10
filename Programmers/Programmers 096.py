# 귤 고르기
def solution(k, tangerine):
    answer = 0

    dict = {}
    for i in tangerine:
        try:
            dict[i] += 1
        except:
            dict[i] = 1

    sorted_dict_list = sorted(
        dict.items(), key=lambda item: item[1])

    while k > 0:
        popped_tangerine = sorted_dict_list.pop()
        k -= popped_tangerine[1]
        answer += 1
    return answer

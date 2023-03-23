# 보석 쇼핑
def solution(gems):
    n = len(gems)
    answer = [0, n - 1]
    gems_kind = len(set(gems))
    gems_dict = {gems[0]: 1, }
    right, left = 0, 0

    while right < n and left < n:
        if len(gems_dict) < gems_kind:
            right += 1
            if right == n:
                break
            gems_dict[gems[right]] = gems_dict.get(gems[right], 0) + 1

        else:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            if gems_dict[gems[left]] == 1:
                del gems_dict[gems[left]]
            else:
                gems_dict[gems[left]] -= 1
            left += 1
    answer[0] += 1
    answer[1] += 1

    return answer

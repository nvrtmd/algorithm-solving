# 스킬트리
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        curr_skill_idx = 0
        for s in skill_tree:
            if s in skill:
                if s == skill[curr_skill_idx]:
                    curr_skill_idx += 1
                else:
                    break
        else:
            answer += 1
    return answer

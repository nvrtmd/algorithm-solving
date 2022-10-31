# 스킬트리
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        # flag를 사용하여 이중루프 제어
        flag = True
        # skill 순서를 거꾸로 뒤집음
        reversed_skill_order = list(skill[::-1])
        for skl in skill_tree:
            # 만약 스킬이 스킬 순서 내에 존재하는데 스킬 순서와 맞지 않으면
            if skl in reversed_skill_order and skl != reversed_skill_order[-1]:
                # flag를 false로 변환 후 내부루프 탈출
                flag = False
                break
            # 만약 스킬이 스킬 순서에 맞다면
            if skl == reversed_skill_order[-1]:
                # 해당 스킬을 스킬 순서 리스트에서 제거
                reversed_skill_order.pop()
            # 만약 스킬이 순서대로 나열되어 있다면
            if len(reversed_skill_order) <= 0:
                # 내부루프 탈출
                break
        # 내부루프 탈출 시 flag가 True인 상태라면 = 스킬이 순서대로 나열된 상태라면
        if flag:
            # answer에 1 더하기
            answer += 1

    return answer

# 대충 만든 자판
def solution(keymap, targets):
    answer = []

    for target in targets:
        clicked = 0
        for s in target:
            minimum = 101
            for key in keymap:
                try:
                    minimum = min(minimum, key.index(s) + 1)
                except:
                    continue
            else:
                if minimum < 101:
                    clicked += minimum
                else:
                    clicked = -10000
        if clicked <= 0:
            answer.append(-1)
        else:
            answer.append(clicked)
    return answer

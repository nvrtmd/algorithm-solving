# 추억 점수
def solution(name, yearning, photo):
    answer = []

    yearning_dict = {}
    for name, yearn in zip(name, yearning):
        yearning_dict[name] = yearn

    for i in photo:
        temp = 0
        for j in i:
            try:
                temp += yearning_dict[j]
            except:
                pass
        answer.append(temp)
    return answer

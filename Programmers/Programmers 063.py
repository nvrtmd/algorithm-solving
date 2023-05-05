# 성격 유형 검사하기
def solution(survey, choices):
    answer = []
    attributes_dict_arr = [{"R": 0, "T": 0}, {"C": 0, "F": 0},
                           {"J": 0, "M": 0}, {"A": 0, "N": 0}]

    attributes_arr = ["RT", "CF", "JM", "AN"]

    for attributes, choice in zip(survey, choices):
        attribute = ""
        choice_score = 0
        if 4 - choice < 0:
            attribute = attributes[1]
        elif 4 - choice > 0:
            attribute = attributes[0]

        choice_score = abs(4 - choice)
        for mbti_attributes_dict in attributes_dict_arr:
            if attribute in mbti_attributes_dict.keys():
                mbti_attributes_dict[attribute] += choice_score

    for attributes in attributes_arr:
        for attributes_dict in attributes_dict_arr:
            if attributes[0] in attributes_dict.keys():
                if attributes_dict[attributes[0]] == attributes_dict[attributes[1]]:
                    answer.append(attributes[0])
                else:
                    for i in range(2):
                        if attributes_dict[attributes[i]] == max(attributes_dict.values()):
                            answer.append(attributes[i])

    return ''.join(answer)

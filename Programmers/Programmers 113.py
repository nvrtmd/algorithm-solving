# 옹알이 (2)
def solution(babbling):
    answer = 0
    able_babble_dict = {"aya": '!', "ye": '@', "woo": '$', "ma": '~'}
    for babble in babbling:
        for able in able_babble_dict.keys():
            while True:
                if able in babble:
                    babble = babble.replace(able, able_babble_dict[able])
                else:
                    break
        for i in babble:
            if i not in able_babble_dict.values():
                break
        else:
            for i in ['!!', '@@', '$$', '~~']:
                if i in babble:
                    break
            else:
                answer += 1
    return answer

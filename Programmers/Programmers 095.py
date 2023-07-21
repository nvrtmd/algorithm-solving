# [1차] 다트 게임
def isInt(str):
    try:
        if 0 <= int(str) <= 9:
            return True
        else:
            return False
    except:
        return False


def solution(dartResult):
    operator_dict = {
        'S': 1,
        'D': 2,
        'T': 3,
        '*': 2,
        '#': -1
    }
    num_arr = []
    operator_arr = []

    calculated_result = []
    num = ''
    operator = ''
    for i, result in enumerate(dartResult):
        if isInt(result):
            num += result
            continue
        else:
            if i < len(dartResult) - 1 and isInt(dartResult[i + 1]):
                operator += result
                operator_arr.append(operator)
                num_arr.append(int(num))
                operator = ''
                num = ''
            else:
                operator += result

    operator_arr.append(operator)
    num_arr.append(int(num))

    for num, operator in zip(num_arr, operator_arr):
        for i in operator:
            if i in ["S", "D", "T"]:
                num **= operator_dict[i]
            elif i == '*':
                if len(calculated_result) > 0:
                    calculated_result[-1] *= operator_dict[i]
                num *= operator_dict[i]
            elif i == '#':
                num *= -1

        calculated_result.append(num)
    return sum(calculated_result)

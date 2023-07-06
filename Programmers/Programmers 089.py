# [1차] 비밀지도
def convert(n, m):
    result = ''
    while n > 0:
        n, mod = divmod(n, m)
        result += str(mod)

    return result[::-1]


def extend_length(n, converted):
    return '0' * (n - len(converted)) + converted


def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        converted_a1 = extend_length(n, convert(a1, 2))
        converted_a2 = extend_length(n, convert(a2, 2))
        temp = ""
        for i in range(n):
            if int(converted_a1[i]) + int(converted_a2[i]) == 0:
                temp += ' '
            else:
                temp += "#"
        answer.append(temp)
    return answer

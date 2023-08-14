# [3차] n진수 게임 (진법 변환 - 16진법까지)
def convert(target, number):
    result = ''
    num_to_alphabet = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while target > 0:
        target, mod = divmod(target, number)
        if number > 10 and 10 <= mod <= 15:
            result += str(num_to_alphabet[mod])
        else:
            result += str(mod)

    return result[::-1]


def solution(n, t, m, p):
    converted_numbers = '0'
    answer = ""

    for i in range(t * m):
        converted = convert(i, n)
        converted_numbers += converted

    target_index = p - 1
    for index, number in enumerate(converted_numbers):
        if len(answer) == t:
            return answer
        if index == target_index:
            answer += number
            target_index += m

    return answer

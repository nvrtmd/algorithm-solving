# 2개 이하로 다른 비트
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


def solution(numbers):
    answer = []
    for number in numbers:
        if number == 0:
            answer.append(1)
            continue
        converted = convert(number, 2)
        arr = list(converted)
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] == '0':
                try:
                    arr[i + 1] = '0'
                except:
                    pass
                arr[i] = '1'
                break
        else:
            arr[0] = '0'
            arr = ['1'] + arr

        target = 0
        for idx, num in enumerate(arr[::-1]):
            target += (2 ** int(idx)) * int(num)
        else:
            answer.append(target)

    return answer

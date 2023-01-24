# 숫자 문자열과 영단어
def solution(s):
    answer = ''
    number_dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    word = ''

    for i in range(len(s)):
        if s[i] in number_dict.keys():
            answer += s[i]
            continue
        if word not in number_dict.values():
            word += s[i]
            for key, value in number_dict.items():
                if value == word:
                    answer += key
                    word = ''

    return int(answer)

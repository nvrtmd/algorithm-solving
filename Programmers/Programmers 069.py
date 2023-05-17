# 이상한 문자 만들기
def solution(s):
    answer = ''

    flag = 0
    for i in s:
        if i != ' ':
            if flag % 2 != 0:
                answer += i.lower()
            else:
                answer += i.upper()
            flag += 1
        else:
            if flag:
                flag = 0
            answer += i

    return answer

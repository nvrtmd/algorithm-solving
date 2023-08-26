# 문자열 나누기
def solution(s):
    answer = 0
    target = ''
    dic = {'other': 0}
    for i in s:
        if target == '':
            target = i
            dic[target] = 1
            continue
        else:
            if i != target:
                dic['other'] += 1
            else:
                dic[target] += 1

        if dic[target] == dic['other']:
            target = ''
            dic = {'other': 0}
            answer += 1

    return answer if len(dic) == 1 else answer + 1

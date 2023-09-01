# 둘만의 암호
def solution(s, skip, index):
    answer = ''
    s_arr = []
    skip_arr = []
    for i in s:
        s_arr.append(ord(i))
    for i in skip:
        skip_arr.append(ord(i))

    for s_ord in s_arr:
        for i in range(index):
            s_ord += 1
            if s_ord > 122:
                s_ord -= 26

            while s_ord in skip_arr:
                s_ord += 1
                if s_ord > 122:
                    s_ord -= 26
        else:
            while s_ord in skip_arr:
                s_ord += 1
                if s_ord > 122:
                    s_ord -= 26

        answer += chr(s_ord)

    return answer

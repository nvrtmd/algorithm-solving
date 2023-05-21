# 시저 암호
def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
            continue

        pushed = ord(i) + n
        if 97 <= ord(i) < 123:
            if pushed > 122:
                answer += chr(pushed - 123 + 97)
            else:
                answer += chr(ord(i) + n)
        else:
            if pushed > 90:
                answer += chr(pushed - 91 + 65)
            else:
                answer += chr(ord(i) + n)

    return answer

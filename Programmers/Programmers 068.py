# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    s = ' ' + s
    for i in range(1, len(s)):
        curr_word = s[i]
        try:  # 첫 글자가 숫자
            int(curr_word)
        except:  # 첫 글자가 문자
            if s[i - 1] == ' ':
                curr_word = curr_word.upper()
            else:
                curr_word = curr_word.lower()
        answer += curr_word
    return answer

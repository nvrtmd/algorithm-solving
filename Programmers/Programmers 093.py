# 괄호 회전하기
# 올바른 괄호 판단 함수
def correct_pair(s):
    # 괄호가 들어갈 스택
    paren_stack = []
    left_parens_arr = ["(", "[", "{"]
    correct_pairs_arr = ["()", "[]", "{}"]
    # 괄호 순회
    for paren in s:
        # 만약 스택에 아무것도 들어있지 않다면
        if len(paren_stack) <= 0:
            # '('는 스택에 넣기
            if paren in left_parens_arr:
                paren_stack.append(paren)
            # ')'는 짝을 맞출 수 없으므로 False 리턴
            else:
                return False
        # 스택이 비어있지 않다면
        else:
            # 현재 순회하는 괄호가 '('이면 스택에 넣기
            if paren in left_parens_arr:
                paren_stack.append(paren)
            # 현재 순회하는 괄호가 ')'이면 스택의 가장 마지막 요소를 제거(=짝 맞춤 완료)
            else:
                if paren_stack[-1] + paren in correct_pairs_arr:
                    paren_stack.pop()
    # 만약 스택에 남아있는 요소가 있다면 (=괄호들의 짝이 맞지 않음)
    if len(paren_stack) > 0:
        return False
    return True


def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        left = s.pop(0)
        s += left
        if correct_pair(''.join(s)):
            answer += 1
    return answer

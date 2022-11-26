# 짝지어 제거하기
def solution(s):
    string_stack = []

    for i in s:
        # 만약 stack에 요소가 없거나 stack의 최상단 요소가 i와 다르다면
        if len(string_stack) < 1 or string_stack[-1] != i:

            # i를 stack에 추가
            string_stack.append(i)

        # 그렇지 않으면 stack의 최상단 요소를 pop
        else:
            string_stack.pop()

    return int(string_stack == [])

# 사전순 부분문자열
def solution(s):
    string_stack = []

    for i in s:
        # string_stack이 비어있지 않으며, stack의 최상단 요소가 i보다 작으면
        # 최상단 요소를 pop
        # (알파벳끼리 비교했을 때 더 작은 쪽이 사전 순으로 우선)
        while string_stack and string_stack[-1] < i:
            string_stack.pop()
        # 최상단 요소가 i보다 크면 i보다 사전 순으로 더 뒤에 나오므로
        # i를 stack에 추가
        string_stack.append(i)

    return ''.join(string_stack)


def solution(s):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alphabet_dict = {}

    for index, alphabet in enumerate(alphabet_list):
        alphabet_dict[alphabet] = index

    string_stack = []

    for i in s:
        if len(string_stack) < 1 or string_stack[-1] >= i:
            # if len(string_stack) < 1 or alphabet_dict[string_stack[-1]] >= alphabet_dict[i]:
            string_stack.append(i)

        else:
            for _ in range(len(string_stack)):
                if alphabet_dict[string_stack[-1]] < alphabet_dict[i]:
                    string_stack.pop()
                else:
                    break
            string_stack.append(i)

    answer = ''.join(string_stack)
    return answer

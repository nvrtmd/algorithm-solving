# 여행경로
def solution(tickets):
    answer = []
    dic = {}
    stack = ["ICN"]
    for ticket in tickets:
        a, b = ticket
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
    for key, value in dic.items():
        dic[key] = sorted(value, reverse=True)

    while stack:
        top = stack.pop()
        if top not in dic or not dic[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(dic[top].pop())

    return answer[::-1]

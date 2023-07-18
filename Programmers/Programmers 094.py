# n^2 배열 자르기
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        share, remainder = divmod(i, n)
        answer.append(max(share, remainder) + 1)
    return answer

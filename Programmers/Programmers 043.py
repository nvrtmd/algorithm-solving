# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        aliquot = 0
        for i in range(1, num + 1):
            if num % i == 0:
                aliquot += 1
        if aliquot % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer

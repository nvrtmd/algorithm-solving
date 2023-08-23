# 기사단원의 무기
def aliquot(n):  # 약수 개수 구하는 함수
    answer = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)
    return len(answer)


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        num = aliquot(i)
        if num > limit:
            answer += power
        else:
            answer += num
    return answer

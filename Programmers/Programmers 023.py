# 예산 소팅
def solution(d, budget):
    answer = 0

    # 최대한 많은 부서에 물품을 구매해주려면
    # 필요한 금액이 적은 부서부터 구매해주면 되므로
    # 부서 별 신청 금액 배열을 오름차순으로 정렬
    d = sorted(d)

    # 신청 금액 배열 순회
    for i in d:
        # 만약 신청 금액이 buget(예산)보다 작거나 같으면
        if i <= budget:
            # buget에서 신청 금액을 빼고
            # 물품을 지원해줄 수 있는 부서의 개수에 1을 추가
            budget -= i
            answer += 1

        # 예산이 0이 되면 break로 반복문 탈출
        if budget == 0:
            break

    return answer

# 기능개발
import math


def solution(progresses, speeds):
    # 최소 작업일을 담을 변수 선언 및 초기화
    # 해당 변수는 작업이 먼저 완료되어야 할 선행 작업보다 남은 작업일이
    # 더 많은지, 적은지 판단하기 위한 기준으로 사용됨
    minimum_work_day = 0
    answer = []

    # 두 배열로부터 요소 하나씩을 병렬하게 사용
    for progressed, speed in zip(progresses, speeds):
        # 작업 별 남은 작업일을 구하기 위해
        # 100에서 작업 완료 퍼센티지를 뺀 값을 하루에 작업 가능한 양으로 나눔(올림)
        work_day = math.ceil((100 - progressed) / speed)

        # 만약 작업일이 최소 작업일보다 클 경우,
        # 즉, 선행 작업의 남은 작업일보다 현재 선택된 작업의 남은 작업일이 클 경우
        # 선행 작업이 완료된 후에 해당 작업이 완료되어 배포될 것이므로
        # 배포가 이루어질 총 횟수가 1 증가하며, 해당 배포일에 해당 작업 1개가 배포되게 됨
        # 해당 작업의 작업일을 최소 작업일로 갱신(다음 선택될 작업의 남은 작업일과 비교하게 됨)
        # answer에 1을 append
        if work_day > minimum_work_day:
            minimum_work_day = work_day
            answer.append(1)

        # 만약 작업일이 최소 작업일보다 작거나 같을 경우,
        # 즉, 선행 작업보다 먼저 작업이 완료되는 경우
        # 선행 작업이 완료될 때까지 기다렸다가 선행 작업이 배포되는 날 같이 배포될 것이므로
        # answer의 가장 마지막 요소(선행 작업의 배포일에 배포될 작업 개수)에 1을 추가
        else:
            answer[-1] += 1

    return answer

# 실패율
def solution(N, stages):
    answer = []
    fail_rate_array = []

    for stage_number in range(1, N + 1):
        success = 0
        failed = 0
        for stage in stages:
            if stage == stage_number:
                failed += 1
            elif stage > stage_number:
                success += 1
        try:
            failed_rate = failed / (failed + success)
        except:
            failed_rate = 0

        fail_rate_array.append([stage_number, failed_rate])

    fail_rate_array = sorted(fail_rate_array, key=lambda x: x[1], reverse=True)

    for fail_rate in fail_rate_array:
        answer.append(fail_rate[0])

    return answer

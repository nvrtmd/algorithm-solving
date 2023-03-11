# 입국심사
def solution(n, times):
    start = min(times)
    end = max(times) * n

    while start < end:
        mid = (start + end) // 2
        customer = 0
        for time in times:
            customer += mid // time
        if customer >= n:
            end = mid
        else:
            start = mid + 1
    return start

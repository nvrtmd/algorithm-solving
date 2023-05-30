# 멀리 뛰기
def solution(n):
    memo = [0 for _ in range(n)]

    for i in range(n):
        if i < 2:
            memo[i] = i + 1
        else:
            memo[i] = (memo[i - 2] + memo[i - 1]) % 1234567
    return memo[n-1]

def solution(n):
    arr = [1, 2]
    for i in range(n):
        if i < 2:
            continue
        else:
            arr.append((arr[i-2] + arr[i - 1]) % 1234567)
    return arr[n-1]

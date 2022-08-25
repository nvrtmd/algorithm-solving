# 어떠한 수 n이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 단, 두 번째 연산은 n이 k로 나누어 떨어질 때만 선택할 수 있다.

# 1. n에서 1을 뺀다.
# 2. n을 k로 나눈다.

# n과 k가 주어질 때 n이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하라.


# ------------------------------------------------------
# 해설을 참고한 풀이

n = int(input())
k = int(input())
answer = 0
while n >= k:
    target = (n//k) * k
    answer += (n - target)
    n = (target // k)
    answer += 1


answer += (n - 1)
print(answer)


# ------------------------------------------------------
# 스스로 풀이

n = int(input())
k = int(input())
answer = 0
while n >= k:
    answer += 1
    n //= k
    answer += (n % k)

answer += n - 1
print(answer)

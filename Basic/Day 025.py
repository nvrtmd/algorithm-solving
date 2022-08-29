# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.


# ------------------------------------------------------


# 나의 풀이

n = int(input())

answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                answer += 1

print(answer)


# 수정 풀이

n = int(input())

answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1


print(answer)

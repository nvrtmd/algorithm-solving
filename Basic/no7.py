# “무어의 법칙”이란 인터넷 경제의 3원칙 가운데 하나로, 마이크로칩의 성능이 일정한 기간을 간격으로 두 배씩 증가한다는 경험적인 예측입니다.
# 한 연구소에서 이 법칙을 증명하기 위해 마이크로칩이 2MB일 때부터 기록해오고 있습니다. 처음에는 2, 두 번째 기록은 4, …, ii 번째 기록은 2^i2i과같이 기록되어 있습니다.
# 어느 날, 한 연구원의 조카가 이 연구소에 놀러 와 마이크로칩의 성능을 기록해 놓은 것을 보았습니다. 큰 수는 읽을 수 없는 조카는 기록을 보며 각 자릿수를 더하며 놀았습니다.
# 예를 들어, 14번째 기록을 보았다면 22가 됩니다.
# 2^{14} = 16384, 1 + 6 + 3 + 8 + 4 = 222
# 14 =16384,1+6+3+8+4=22
# 조카가 N 번째 기록을 보면서 각 자릿수를 더했을 경우, 어떤 수가 될지 구하는 프로그램을 작성하세요.

# [입력]
# 자연수 N을 입력합니다.
# (1<=N<=10,000)
# (1<=N<=10,000)

# [출력]
# N 번째 기록을 보고 각 자리수를 더한 값을 출력합니다.


# ------------------------------------------------------


num = int(input())

k = 2 ** num
result = 0
for i in range(len(str(k))):
    p = str(k)[i]
    result += int(p)
print(result)

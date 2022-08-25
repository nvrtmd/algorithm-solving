# 직각삼각형
# 세 변의 길이가 주어졌을 때 이 삼각형이 직각 삼각형인지 아닌지를 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄부터 삼각형의 세 변의 길이를 공백을 기준으로 입력합니다.
# 마지막 줄에는 입력이 끝을 의미하는 0을 입력합니다.
# ※ 변의 길이는 1,000보다 작거나 같은 자연수이며 테스트 케이스는 3개를 넘지 않습니다.

# [출력]
# 첫 번째 줄부터 입력한 세 변의 길이에 대해 직각삼각형이 맞으면 ‘rightangle’, 아니면 ‘triangle’를 출력합니다.

l = []

for i in range(3):
    a = input()
    if a[0] == '0':
        break
    b, c, d = map(int, a.split())
    k = []
    k = list((b, c, d))
    k.sort()
    if int(k[0]) ** 2 + int(k[1]) ** 2 == int(k[2]) ** 2:
        l.append('rightangle')
    else:
        l.append('triangle')


for j in range(len(l)):
    print(l[j])

# 떡 먹은 떡만이
# 똑같이 생긴 세쌍둥이 떡만이 1, 떡만이 2, 떡만이 3이 일렬로 서있습니다. 세 떡만이가 처음에 서 있던 자리를 왼쪽부터 1번, 2번, 3번 자리라고 합니다.
# 떡만이 1은 하나밖에 없는 떡을 한입에 먹어버렸습니다. 그리고 세 떡만이들은 누가 떡을 먹었는지 숨기기 위해 서로 자리를 바꾸려고 합니다.
# 떡만이들은 두 자리를 고른 다음 두 자리에 있는 떡만이들이 자리를 바꾸려고 합니다. 예를 들어, 1번 자리와 3번 자리를 골랐다면 1번 자리에 있는 떡만이가 3번 자리에, 3번 자리에 있던 떡만이가 1번 자리로 이동하게 됩니다.
# 떡만이들이 자리를 M 번 바꾼다고 할 때, 떡 먹은 떡만이를 찾는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 위치를 바꾼 횟수를 나타내는 자연수 M을 입력합니다.
# (1<=\ M<=100)
# (1<= M<=100)
# 둘째 줄부터 M개의 줄에는 위치를 바꾼 자리 X와 Y를 공백으로 구분하여 입력합니다.
# X와 Y는 1, 2, 3만 입력 가능합니다.
# X와 Y의 값은 3보다 작거나 같고, X와 Y가 같을 수도 있습니다.

# [출력]
# 떡을 먹은 용만이가 위치한 곳의 자리 번호를 출력합니다.


# ------------------------------------------------------


ddeokman = [0, 1, 2, 3]
change_num = int(input())
change_series = []
for i in range(change_num):
    j, k = map(int, input().split())
    change_series.append(j)
    change_series.append(k)

tamp = 0
for l in range(change_num):
    temp = ddeokman[change_series[l * 2]]
    ddeokman[change_series[l * 2]] = ddeokman[change_series[l * 2 + 1]]
    ddeokman[change_series[l * 2 + 1]] = temp


print(ddeokman.index(1))

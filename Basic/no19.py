# 훌라후프
# 코더 초등학교의 학생들은 체육 시간에 훌라후프를 이용하여 수업하였습니다. 아이들의 덩치는 제각각이기에 훌라후프의 크기 역시 제각각이었습니다.
# 수업이 끝나고 선생님은 N개의 훌라후프를 수거하여 각각의 훌라후프가 앞에 있는 훌라후프와 뒤에 있는 훌라후프가 접하도록 바닥에 내려놓았습니다.
# 장난을 좋아하는 체셔는 첫 번째 훌라후프를 돌리기 시작했고, 나머지 훌라후프도 같이 돌아간다는 사실을 발견했습니다. 이렇게 장난을 치다 보니 첫 번째 훌라후프를 한 바퀴 돌리면, 나머지 훌라후프는 몇 바퀴 도는지 궁금해졌습니다.
# 각각의 훌라후프의 반지름이 주어졌을 때, 첫 번째 훌라후프를 한 바퀴 돌리면, 나머지 훌라후프는 몇 바퀴 돌아가는지 구하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 훌라후프의 개수를 나타내는 자연수 N을 입력합니다.
# (3 ≤ N ≤ 100)
# (3≤N≤100)
# 다음 줄에는 훌라후프의 반지름을 선생님이 바닥에 놓은 순서대로 입력합니다. 반지름은 1과 1000을 포함하는 사이의 자연수입니다.

# [출력]
# 출력은 총 N-1 줄입니다. 첫 번째 훌라후프를 제외한 각각의 훌라후프에 대해서, 첫 번째 훌라후프를 한 바퀴 돌리면 그 훌라후프는 몇 바퀴 도는지 기약 분수 형태 A/B로 출력합니다.


# ------------------------------------------------------


# math 모듈 사용하지 않고 풀려고 한 흔적... 이건 80점밖에 안나옴
# circle_num = int(input())
# circles = list(map(int, input().split()))
# denominator = circles[0]

# for i in range(1, circle_num):
#     if denominator >= circles[i]:
#         if denominator % circles[i] == 0:
#             answ_deno = denominator // circles[i]
#             print(str(answ_deno) + '/' + '1')
#         elif denominator % (denominator % circles[i]) == 0 and circles[i] % (denominator % circles[i]) == 0:
#             gcd = denominator % circles[i]
#             answ_deno = denominator // gcd
#             answ_nume = circles[i] // gcd
#             print(str(answ_deno) + '/' + str(answ_nume))
#         else:
#             print(str(denominator) + '/' + str(circles[i]))
#     else:
#         if circles[i] % denominator== 0:
#             answ_nume = circles[i] // denominator
#             print('1' + '/' + str(answ_nume) )
#         elif denominator % (circles[i]  % denominator) == 0 and circles[i] % (circles[i]  % denominator) == 0:
#             gcd = circles[i] % denominator
#             answ_deno = denominator // gcd
#             answ_nume = circles[i] // gcd
#             print(str(answ_deno) + '/' + str(answ_nume))
#         else:
#             print(str(denominator) + '/' + str(circles[i]))

import math

circle_num = int(input())
circles = list(map(int, input().split()))
denominator = circles[0]

for i in range(1, circle_num):
    gcd = math.gcd(denominator, circles[i])
    if gcd == 1:
        print(str(denominator) + '/' + str(circles[i]))
    else:
        answ_deno = denominator // gcd
        answ_nume = circles[i] // gcd
        print(str(answ_deno) + '/' + str(answ_nume))

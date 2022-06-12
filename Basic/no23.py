# 마을에 모험가가 n명이 있다. 모험가 길드에서는 n명의 모험가를 대상으로 공포도를 측정했다.
# 모험가 그룹을 안전하게 구성하기 위해 공포도가 x인 모험가는 반드시 x명 이상으로 구성된 그룹에 포함된다.
# 최대 몇 개의 모험가 그룹이 만들어질 수 있는가? 만들어질 수 있는 그룹 수의 최댓값을 구하라.


# ------------------------------------------------------


n = int(input())
fear_data = list(map(int, input().split()))
fear_data.sort()

answer = 0
wait_list = []
for fear in fear_data:
    wait_list.append(fear)
    if fear <= len(wait_list):
        answer += 1
        wait_list.clear()

print(answer)

# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 4153
while True:
    num_list = list(map(int, input().split()))
    if 0 in num_list:
        break

    longest = max(num_list)
    num_list.remove(longest)
    if num_list[0] ** 2 + num_list[1] ** 2 == longest ** 2:
        print('right')
    else:
        print('wrong')

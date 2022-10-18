# BOJ 단계별로 풀어보기
# 11. 브루트 포스

# 1018
n, m = map(int, input().split())
ls = []
for i in range(n):
    ls.append(input())

b_first = [] + ['BWBWBWBW', 'WBWBWBWB'] * 4
w_first = [] + ['WBWBWBWB', 'BWBWBWBW'] * 4

cnt_list = []
for i in range(n - 7):
    for j in range(m - 7):
        b_first_cnt = 0
        w_first_cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ls[k][l] != b_first[k - i][l - j]:
                    b_first_cnt += 1
                if ls[k][l] != w_first[k - i][l - j]:
                    w_first_cnt += 1
        cnt_list.append(b_first_cnt)
        cnt_list.append(w_first_cnt)

print(min(cnt_list))

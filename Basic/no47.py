# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 2562
input_list = []
for i in range(9):
    num = int(input())
    input_list.append(num)
max_num = max(input_list)
print(max_num)
print(input_list.index(max_num) + 1)

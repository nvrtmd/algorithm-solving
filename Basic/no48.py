# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 2577
num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = 1
for i in range(3):
    num *= int(input())

num_to_str = str(num)
for i in range(len(num_to_str)):
    index = int(num_to_str[i])
    num_list[index] += 1

for i in range(len(num_list)):
    print(num_list[i])

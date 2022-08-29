# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 3052
num_list = []
result = 0
for i in range(42):
    num_list.append(0)

for i in range(10):
    num = int(input())
    index = num % 42
    if num_list[index] == 0:
        num_list[index] += 1

for i in range(42):
    result += num_list[i]

print(result)

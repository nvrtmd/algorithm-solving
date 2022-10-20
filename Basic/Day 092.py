# BOJ 단계별로 풀어보기
# 12. 정렬

# 2750
n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    if len(num_list) == 0:
        num_list.append(num)
        continue
    for j in range(len(num_list)):
        if num > num_list[j]:
            if j == len(num_list) - 1:
                num_list.append(num)
            continue
        else:
            num_list.insert(j, num)
            break

for i in num_list:
    print(i)

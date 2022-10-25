# BOJ 단계별로 풀어보기
# 12. 정렬

# 1427
n = input()
num_list = []
for i in n:
    num_list.append(i)

num_list.sort(reverse=True)

print("".join(num_list))

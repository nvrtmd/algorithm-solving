# BOJ 단계별로 풀어보기
# 12. 정렬

# 2751
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

for i in sorted(array):
    print(i)

# BOJ 단계별로 풀어보기
# 11. 브루트 포스

# 7568
n = int(input())
body = []
rank = []
for i in range(n):
    height, weight = map(int, input().split())
    body.append((height, weight))

for i in range(n):
    count = 1
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            count += 1
    rank.append(count)

for i in rank:
    print(i, end=" ")

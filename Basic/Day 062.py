# BOJ 단계별로 풀어보기
# 7. 문자열

# 2908
a, b = map(str, input().split())

new_a = ""
new_b = ""

for i in range(len(a) - 1, -1, -1):
    new_a += a[i]
    new_b += b[i]

print(max([new_a, new_b]))

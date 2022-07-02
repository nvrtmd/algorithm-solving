# BOJ 단계별로 풀어보기
# 3. for문

# 10871
n, x = map(int, input().split())
a = list(map(int, input().split()))
result = []
for i in range(n):
    if a[i] < x:
        result.append(str(a[i]))

print(" ".join(result))

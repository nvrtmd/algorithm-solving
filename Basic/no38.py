# BOJ 단계별로 풀어보기
# 3. for문

# 11021
n = int(input())
result = []
for i in range(n):
    a, b = map(int, input().split())
    result.append(a+b)

for i in range(n):
    print(f"Case #{i+1}: {result[i]}")

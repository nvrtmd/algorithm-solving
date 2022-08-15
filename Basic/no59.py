# BOJ 단계별로 풀어보기
# 7. 문자열

# 2675
n = int(input())

for i in range(n):
    count, word = input().split()
    result = ""
    for j in word:
        result += j * int(count)
    print(result)

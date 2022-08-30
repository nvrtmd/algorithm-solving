# BOJ 단계별로 풀어보기
# 7. 문자열

# 1316
n = int(input())
result = n
for i in range(n):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break

print(result)

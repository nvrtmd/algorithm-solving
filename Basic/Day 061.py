# BOJ 단계별로 풀어보기
# 7. 문자열

# 1152
sentence = list(input().split())
word_dict = {}
for i in sentence:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

result = 0
for values in word_dict.values():
    result += values
print(result)

# BOJ 단계별로 풀어보기
# 7. 문자열

# 1157
word = input().upper()
word_dict = {}
for i in word:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

most_frequent = [k for k, v in word_dict.items() if max(
    word_dict.values()) == v]

if len(most_frequent) > 1:
    print("?")
else:
    print(most_frequent[0])

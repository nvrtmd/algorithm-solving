# BOJ 단계별로 풀어보기
# 7. 문자열

# 2941
croatia = {"c=": 0, "c-": 0, "dz=": 0, "d-": 0,

           "lj": 0, "nj": 0, "s=": 0, "z=": 0, "other": 0}
word = input()
result = 0

for i in croatia.keys():
    if i in word:
        word = word.replace(i, ".")

result = len(word)

print(result)

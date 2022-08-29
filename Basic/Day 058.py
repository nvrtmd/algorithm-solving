# BOJ 단계별로 풀어보기
# 7. 문자열

# 10809
word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in range(len(alphabet)):
    result.append('-1')

for i in alphabet:
    if i in word:
        index_in_word = word.index(i)
        index_in_alphabet = alphabet.index(i)
        result[index_in_alphabet] = str(index_in_word)

print(" ".join(result))

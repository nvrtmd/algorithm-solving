# BOJ 단계별로 풀어보기
# 7. 문자열

# 5622
alphabets = [[], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], [
"M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]

input_alphabets = input()
result = 0

for i in input_alphabets:
    for j in alphabets:
        if i in j:
            result += alphabets.index(j) + 2

print(result)

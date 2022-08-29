# BOJ 단계별로 풀어보기
# 5. 1차원 배열

# 8958
n = int(input())
ox_list = []
result_list = []
for i in range(n):
    ox_list.append(input())

for i in range(n):
    result = 0
    current_grade = 0

    for j in range(len(ox_list[i])):
        ox = ox_list[i]
        if ox[j] == 'O':
            current_grade += 1
            result += current_grade
        else:
            current_grade = 0
    result_list.append(result)

for i in range(n):
    print(result_list[i])

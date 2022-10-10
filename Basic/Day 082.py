# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 3009
x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    if x in x_list:
        x_list.remove(x)
    else:
        x_list.append(x)
    if y in y_list:
        y_list.remove(y)
    else:
        y_list.append(y)

for i in range(len(x_list)):
    print(f"{x_list[0]} {y_list[0]}")

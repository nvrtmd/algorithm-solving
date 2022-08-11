# BOJ 단계별로 풀어보기
# 6. 함수

# 1065
def sol(num):
    if num < 100:
        return True

    num_to_str = str(num)

    for i in range(len(num_to_str)-2):
        if int(num_to_str[i+1]) - int(num_to_str[i]) == int(num_to_str[i+2]) - int(num_to_str[i+1]):
            continue
        else:
            return False
    return True


n = int(input())
result = 0
for i in range(1, n + 1):
    if sol(i):
        result += 1

print(result)

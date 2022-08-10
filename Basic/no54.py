# BOJ 단계별로 풀어보기
# 6. 함수

# 4673
def d(num):
    result = 0
    num_to_str = str(num)
    if num < 10:
        result = num * 2
    else:
        result = num
        for i in range(len(num_to_str)):
            result += int(num_to_str[i])

    return result


m = []
for i in range(10000):
    if d(i) <= 10000:
        m.append(d(i))

m = sorted(m)
for i in range(1, 10001):
    if i in m:
        pass
    else:
        print(i)

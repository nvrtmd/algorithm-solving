# BOJ 단계별로 풀어보기
# 11. 브루트 포스

# 1436
n = int(input())
ls = []
num = 666
while num >= 666:
    if '666' in str(num):
        ls.append(num)
    if len(ls) == n:
        print(ls[n - 1])
        break
    num += 1

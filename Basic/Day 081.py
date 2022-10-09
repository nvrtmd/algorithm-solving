# BOJ 단계별로 풀어보기
# 9. 기본 수학 2

# 1085
x, y, w, h = map(int, input().split())
num_list = [x, w-x, y, h-y]
print(min(num_list))

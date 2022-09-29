# BOJ 단계별로 풀어보기
# 8. 기본 수학 1

# 10250
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        room_num = n // h
        floor = h
    else:
        room_num = n // h + 1
        floor = n % h
    if room_num < 10:
        print(f"{floor}0{room_num}")
    else:
        print(f"{floor}{room_num}")

# BOJ 단계별로 풀어보기
# 12. 정렬

# 2108
import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
num_list.sort()
medium = num_list[n // 2]
between = num_list[-1] - num_list[0]
most_frequent_list = Counter(num_list).most_common()
most_frequent = 0
if len(num_list) <= 1:
    most_frequent = num_list[0]
else:
    if most_frequent_list[0][1] == most_frequent_list[1][1]:
        most_frequent = most_frequent_list[1][0]
    else:
        most_frequent = most_frequent_list[0][0]

print("%.f" % (sum(num_list)/n))
print(medium)
print(most_frequent)
print(between)

import sys
import heapq

read = sys.stdin.readline
target_num = int(read().strip())
apply_member_num = list(map(int, read().strip().split()))

if target_num > len(apply_member_num):
    answer = ' '.join(map(str, sorted(set(apply_member_num))))
else:
    answer = []
    duplicated_member_num = set()
    for _ in range(len(apply_member_num)):
        current_member_num = heapq.heappop(apply_member_num)
        if current_member_num not in apply_member_num and current_member_num not in duplicated_member_num:
            answer.append(current_member_num)
        else:
            duplicated_member_num.add(current_member_num)
    answer = ' '.join(map(str, sorted(answer)))
print(answer)

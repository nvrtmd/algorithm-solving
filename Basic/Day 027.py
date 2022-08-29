# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어질 때,
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 모든 숫자를 더한 값을 이어서 출력하라.


# ------------------------------------------------------


n = input()
numbers = []
sum_numbers = 0
alphabets = []
for i in range(10):
    numbers.append(str(i))

for i in n:
    if i in numbers:
        sum_numbers += int(i)
    else:
        alphabets.append(i)


answer = "".join(sorted(alphabets))
if sum_numbers:
    answer + str(sum_numbers)

print(answer)

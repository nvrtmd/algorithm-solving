# 시험
# 파랑, 빨강, 노랑이는 수학 시험을 보았습니다. 이 세 명은 수학의 ‘수’ 자만 들어가도 몸서리를 치기 때문에 모두 수학 시험을 풀지 않고 찍으려고 합니다.
# 다행히 수학 시험은 주관식이 없는 5지 선다형입니다. 같은 점수를 받고 싶지 않았던 셋은 각자의 규칙을 적용해 답을 찍습니다.
# 파랑이는 답을 5432154321…. 로 반복해서 답을 찍습니다.
# 빨강이는 답을 1234512345…. 로 반복해서 답을 찍습니다.
# 노랑이는 답을 3333333333…. 로 반복해서 잡을 찍습니다.
# 시험 문항 수와 답을 줬을 때, 시험에서 가장 많이 맞힌 개수와 맞힌 사람의 이름을 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄에 시험의 문항 수인 자연수 N을 입력합니다.
# 두 번째 줄에 시험의 정답을 입력합니다.
# (1≤N≤100)
# (1≤N≤100)

# [출력]
# 첫 번째 줄에 가장 많은 문제를 맞힌 사람이 몇 개를 맞췄는지 출력합니다.
# 두 번째 줄에 가장 많은 문제를 맞힌 사람이 누구인지 출력합니다.
# ※ 파랑이는 ‘blue’, 빨강이는 ‘red’, 노랑이는 ‘yellow’를 출력합니다. 동점이면 동점자 모두를 출력하되, 빨강 파랑 노랑 순으로 줄을 바꿔 출력합니다.


# ------------------------------------------------------


student_answer_arr = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [3, 3, 3, 3, 3]]

n = int(input())
test_answer = int(input())
number_of_right_answer = 0
number_of_right_answer_arr = []
student_arr = ['red', 'blue', 'yellow']
for i in range(3):
    temp = []
    number_of_right_answer = 0
    for j in range((n//5)+1):
        temp += student_answer_arr[i]
    for k in range(n):
        if str(temp[k]) == str(test_answer)[k]:
            number_of_right_answer += 1
    number_of_right_answer_arr.append(number_of_right_answer)


print(max(number_of_right_answer_arr))

for l in range(3):
    if number_of_right_answer_arr[l] == max(number_of_right_answer_arr):
        print(student_arr[l], end='\n')

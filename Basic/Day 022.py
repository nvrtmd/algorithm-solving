# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 s가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 또는 '+' 연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, 일반적인 계산 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.


s = str(input())

answer = int(s[0])

for i in range(len(s) - 1):
    target = int(s[i+1])
    if answer * target > answer:
        answer *= target
    else:
        answer += target

print(f"만들 수 있는 가장 큰 수는 {answer}입니다.")

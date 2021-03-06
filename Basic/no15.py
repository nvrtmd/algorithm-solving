# 절대 반지
# 도도새는 N개의 반지를 가지고 있습니다. 반지에는 알파벳 대문자로 이루이진 문자열이 새겨져 있습니다. 적힌 문자열은 10자이며 알파벳 대문자로 이루어져 있습니다.
# 도도새가 반지의 적힌 문자열을 읽을 때 항상 시계 방향으로 읽으며 문자열의 시작과 끝이 연결된 형태로 문자가 새겨져 있습니다.
# 도도새가 가지고 있는 반지의 일부는 모자 장수의 것인데, 반지에 새겨진 문자열 중 모자 장수의 별명이 포함되면 모자 장수의 것이라고 합니다.
# 각 반지에 새겨진 문자열을 줬을 때 모자 장수 반지의 개수를 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄에 모자 장수의 별명을 입력합니다. 별명은 알파벳 대문자이며 10자를 넘지 않습니다.
# 두 번째 줄에 도도새가 가지고 있는 반지의 개수인 자연수 N을 입력합니다.
# (1≤N≤5)
# (1≤N≤5)
# 세 번째부터 각 반지에 새겨진 문자열을 한 줄씩 입력합니다.

# [출력]
# 첫 번째 줄에 모자 장수의 반지의 개수를 출력합니다.


# ------------------------------------------------------


nickname = input()
num = int(input())
ring = 0

for i in range(num):
    input_ring_word = input()
    double_word = input_ring_word * 2
    for j in range(len(double_word)):
        if double_word[j] == nickname[0] and double_word[j:j+len(nickname)] == nickname:
            ring += 1
            break

print(ring)

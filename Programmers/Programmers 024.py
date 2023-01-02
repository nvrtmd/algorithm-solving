# 최솟값 만들기
def solution(A, B):
    answer = 0

    # 두 수를 곱한 값들의 합이 가장 작으려면
    # 가장 작은 수와 가장 큰 수를 곱해야 함
    # 따라서 A는 오름차순, B는 내림차순으로 정렬
    A = sorted(A)
    B = sorted(B, reverse=True)

    # 두 배열의 요소들을 서로 곱해서 answer에 더하기
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

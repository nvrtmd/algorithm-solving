# 행렬의 곱셈
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for col_of_arr1, row_array_of_arr1 in enumerate(arr1):
        for col_of_arr2, row_array_of_arr2 in enumerate(arr2):
            for row_of_arr2, col_element_of_arr2 in enumerate(row_array_of_arr2):
                answer[col_of_arr1][row_of_arr2] += row_array_of_arr1[col_of_arr2] * \
                    col_element_of_arr2

    return answer

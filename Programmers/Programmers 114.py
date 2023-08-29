# Diagonal Difference
def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i, j in enumerate(arr):
        print(i, len(j) - i - 1)
        left_to_right += j[i]
        right_to_left += j[len(j) - i - 1]
    return abs(left_to_right - right_to_left)

# 폰켓몬
def solution(nums):
    if len(nums) // 2 <= len(list(set(nums))):
        return len(nums) // 2
    else:
        return len(list(set(nums)))

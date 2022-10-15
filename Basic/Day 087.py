# BOJ 단계별로 풀어보기
# 11. 브루트 포스

# 2798
n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] <= m:
                result.append(nums[i] + nums[j] + nums[k])

print(max(result))

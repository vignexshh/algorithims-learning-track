def minSubArrayLen(target: int, nums):
    currSum = 0
    left = 0
    res = float('inf')
    for right in range(len(nums)):
        currSum += nums[right]

        while currSum >= target:
            res = min(res, right - left + 1)
            currSum -= nums[left]
            left += 1

    return res if res != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))
# print(minSubArrayLen(15, [1,2,3,4,5]))




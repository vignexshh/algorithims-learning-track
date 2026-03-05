def minSubArrayLen(target: int, nums):
    rightSum = 0
    leftSum = 0
    left = 0
    right = 0
    minLen = 1000
    deleteWatch = 0
    deleteWatch2 = 0

    for item in range(len(nums)):
        if leftSum < target:
            leftSum += nums[item]
            left += 1

        if rightSum < target:
            rightSum += nums[len(nums)-1-item]
            right += 1

        if leftSum >= target:
            deleteWatch2 += 1
            minLen = min(minLen, right, left)
            leftSum -= nums[deleteWatch]

        if rightSum >= target:
            deleteWatch += 1
            minLen = min(minLen, right, left)
            rightSum -= nums[-deleteWatch]



            #len(nums) - right


    return 0 if (minLen == 1000) else minLen

print(minSubArrayLen(7, [2,3,1,2,4,3]))
# print(minSubArrayLen(15, [1,2,3,4,5]))




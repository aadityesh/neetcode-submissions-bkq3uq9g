class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        curSum, maxSum = 0, -1001

        for num in nums:

            curSum += num
            maxSum = max(curSum, maxSum)

            if curSum < 0:
                curSum = 0
            

        
        return maxSum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        curSum, maxSum = 0, 0

        for num in nums:

            curSum += num

            if curSum < 0:
                curSum = 0
            
            maxSum = max(curSum, maxSum)

        
        return maxSum
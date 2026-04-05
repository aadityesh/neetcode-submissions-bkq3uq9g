class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        totalSum = (n * (n + 1)) // 2

        inpSum = 0
        for num in nums:
            inpSum += num
        
        return totalSum - inpSum
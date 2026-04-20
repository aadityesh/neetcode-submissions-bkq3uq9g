class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxProd = float("-inf")

        for i in range(n):
            curProd = 1
            for j in range(i, n):
                curProd *= nums[j]
                maxProd = max(maxProd, curProd)
        
        return maxProd
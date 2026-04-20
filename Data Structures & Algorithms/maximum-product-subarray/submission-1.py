class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        def calcMaxProduct(i, j):
            if i > j:
                return 1
            
            return nums[i] * calcMaxProduct(i+1, j)

        maxProd = float("-inf")
        for i in range(n):
            for j in range(i, n):
                maxProd = max(maxProd, calcMaxProduct(i, j))
                print(f"{maxProd} @ {i} @ {j}")
        
        return maxProd
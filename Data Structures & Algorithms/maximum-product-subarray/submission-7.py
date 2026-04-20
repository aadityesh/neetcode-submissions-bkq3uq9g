class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxProd, minProd = 1, 1
        res = float("-inf")

        for i in range(n):
            
            maxProd *= nums[i]
            minProd *= nums[i]

            print(f"{minProd} -- {maxProd}")
            res = max(res, max(maxProd, minProd))
            print(res)
            if maxProd <= 0:
                maxProd = 1
        
        return res
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        xor1, xor2 = 0, 0

        for num in range(n+1):
            xor1 = xor1 ^ num

        for num in nums:
            xor2 = xor2 ^ num
        
        return xor1 ^ xor2


        # n = len(nums)
        # totalSum = (n * (n + 1)) // 2

        # inpSum = 0
        # for num in nums:
        #     inpSum += num
        
        # return totalSum - inpSum
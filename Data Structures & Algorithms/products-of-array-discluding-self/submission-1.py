class Solution:
    def calcSuffixArray(self,nums):
        n = len(nums) 
        suffix = [1] * n
        res = 1
        for i in range(n - 2, -1, -1):
            res = res * nums[i+1]
            suffix[i] = res

        return suffix

    def calcPrefixArray(self, nums):
        n = len(nums) 
        prefix = [1] * n
        res = 1
        for i in range(1, n):
            res = res * nums[i-1]
            prefix[i] = res

        return  prefix

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
         Brute: Nested loops
         Better: calc and store prefix and suffix arrays
        """
        # BETTER

        # result = [0] * len(nums)
        # prefix = self.calcPrefixArray(nums)
        # suffix = self.calcSuffixArray(nums)

        # print(prefix)
        # print(suffix)

        # for i in range(len(nums)):
        #     result[i] = prefix[i] * suffix[i]
        
        # return result


        # BEST
        n = len(nums)
        prefix = self.calcPrefixArray(nums)
        res = 1
        
        for i in range(n-2, -1, -1):
            res = res * nums[i+1]
            prefix[i] *= res
        
        return prefix







class Solution:
    def findMin(self, nums: List[int]) -> int:

        mini = 1001

        for elem in nums:
            mini = min(mini, elem)
        
        return mini
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for index, elem in enumerate(nums):

            if target == elem: return index

        
        return -1
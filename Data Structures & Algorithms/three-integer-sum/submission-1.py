class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
            initialize a set
            get three elements that sum to zero
            sort and store it in set
        """
        n = len(nums)
        unique = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    current_sum = nums[i] + nums[j] + nums[k]
                    if current_sum == 0:
                        current_ls = [nums[i], nums[j], nums[k]]
                        current_ls.sort()
                        unique.add(tuple(current_ls))
        
        return [list(t) for t in unique]



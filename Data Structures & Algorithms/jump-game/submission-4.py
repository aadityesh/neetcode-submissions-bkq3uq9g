class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # n = len(nums)

        # def dfs(i):

        #     if i == n - 1: return True
        #     if nums[i] == 0: return False

        #     for jump in range(1, nums[i]+1):
        #         if dfs(i + jump):
        #             return True

        #     return False
        
        # return dfs(0)

        n = len(nums)
        
        goal = n - 1 # index

        for i in range(n - 1, -1, -1):
            
            if i + nums[i] >= goal:
                goal = i

        return goal == 0



            

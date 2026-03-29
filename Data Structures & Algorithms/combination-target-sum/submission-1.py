class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # self.res = []
        # self.ls = []

        # def dfs(curr_sum, i):

        #     if i >= len(nums) or curr_sum > target: return

        #     if curr_sum == target: 
        #         self.res.append(list(self.ls))
        #         return

        #     self.ls.append(nums[i])
        #     curr_sum += nums[i]
        #     dfs(curr_sum, i)

        #     curr_sum -= self.ls.pop()
        #     dfs(curr_sum, i + 1)

        res = []
        ls = []
        nums.sort()
        def dfs(curr_sum, ls, start):

            if start >= len(nums): return

            if curr_sum == target: 
                res.append(ls.copy())
                return 

            for i in range(start, len(nums)):

                if curr_sum + nums[i] > target: return
                dfs(curr_sum + nums[i], ls + [nums[i]], i)

        dfs(0, ls, 0)
        return res



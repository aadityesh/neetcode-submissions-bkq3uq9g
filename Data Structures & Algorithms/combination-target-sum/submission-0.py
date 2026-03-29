class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []
        self.ls = []
        def dfs(curr_sum, i):

            if i >= len(nums) or curr_sum > target: return

            if curr_sum == target: 
                self.res.append(list(self.ls))
                return

            self.ls.append(nums[i])
            curr_sum += nums[i]
            dfs(curr_sum, i)

            curr_sum -= self.ls.pop()
            dfs(curr_sum, i + 1)

        dfs(0, 0)
        return self.res
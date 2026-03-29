class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        L, R = 0, n -1

        while L < R:

            curr_sum = nums[L] + nums[R]

            if curr_sum == target:
                return [L+1, R+1]

            
            elif curr_sum < target:
                L += 1

            else:
                 R -= 1

        return []
                
        
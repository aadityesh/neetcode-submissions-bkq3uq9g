class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        n = len(nums)

        L = 0
        R = n - 1
        max_area = -1

        while L < R:

            current_height = min(nums[L], nums[R])
            current_breadth = R - L

            current_area = current_height * current_breadth
            max_area = max(current_area, max_area)

            if R > 0 and nums[L] > nums[R]:
                R -= 1
            elif L < n and nums[L] < nums[R]:
                L += 1
            else:
                L += 1
            
        return max_area


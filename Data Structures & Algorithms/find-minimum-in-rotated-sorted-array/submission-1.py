class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            Brute:
                Linear Search - T [O(n)] S [O(1)]
        """
        # mini = 1001

        # for elem in nums:
        #     mini = min(mini, elem)
        
        # return mini

        n = len(nums)
        L, R = 0, n - 1
        mini = 1001

        while L <= R:

            mid = (L + R) // 2

            if nums[L] <= nums[mid]:
                mini = min(mini, nums[L])
                L = mid + 1
            
            elif nums[mid] <= nums[R]:
                mini = min(mini, nums[mid])
                R = mid - 1

        return mini



            
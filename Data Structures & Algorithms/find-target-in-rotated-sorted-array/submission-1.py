class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """

            3,4,5,6,1,2

            L = 6, mid = 1, H = 2
        
        """

        # for index, elem in enumerate(nums):

        #     if target == elem: return index

        
        # return -1

        n = len(nums)
        low, high = 0, n - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target: return mid

            if nums[low] <= nums[mid]:

                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                
                else:
                    low = mid + 1

            if nums[mid] <= nums[high]:

                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid - 1

        return -1






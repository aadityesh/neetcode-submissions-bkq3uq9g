class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
            Brute:
                Sorting and check for continuous elems

            Better: 
                
        
        """
        # n = len(nums)

        # if n == 0 or n == 1: return n

        # curr = 1
        # longest = 1

        # nums.sort()
        # print(nums)
        # for i in range(n-1):
        #     if nums[i] == (nums[i+1] - 1):
        #         curr += 1
        #         longest = max(longest, curr)
        #     elif nums[i] == nums[i+1]:
        #         continue
        #     else:
        #         curr = 1
        
        # return longest


        # n = len(nums)

        # if n == 0: return 0

        # unique = set(nums)
        # curr = 1
        # longest = 1

        # for elem in nums:
        #     start = elem - 1 # left exists? if not then start of seq
        #     if start not in unique:
        #         next_elem = elem + 1
        #         while next_elem in unique:
        #             next_elem += 1
        #             curr += 1
        #             longest = max(longest, curr)
        #         else:
        #             curr = 1
            
        # return longest


        n = len(nums)
        if n == 0 or n == 1: return n

        longest = 1
        for i in range(n):

            next_elem = nums[i] + 1
            curr = 1
            
            while next_elem in nums:
                curr += 1
                longest = max(longest, curr)
                next_elem += 1
        
        return longest



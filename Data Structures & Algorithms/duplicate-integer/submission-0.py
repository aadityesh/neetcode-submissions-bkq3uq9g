class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
       """
       # Brute: 
       You stand on each element and look on its right to find one more
       occurence of it

       T/S: n^2/constant

       
       # Best:
       Sort and try to match adjacent elements
       T/S: nlogn/constant
       """

       nums.sort()
       for i in range(len(nums) - 1):
          #   print(i)
            if nums[i] == nums[i+1]: return True

       return False
        
        
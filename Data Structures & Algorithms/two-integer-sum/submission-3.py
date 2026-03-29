class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
            Brute: 
                Stand on each element (i) and look towards its right
                for next element (j) that will sum up t target

                T/S: O(N^2)/O(1)

            
            Better:
                Iterate over the array and stand on elem (j), find the difference
                and look for it in the hash

                 T/S: O(N)/O(N)
        
        """

        # Brute

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []


        # Better:

        hash_nums = {}
        for index in range(len(nums)):
            elem = nums[index]
            difference = target - elem # elem is j here, difference is i
            if difference in hash_nums:
                return [hash_nums[difference], index]

            hash_nums[elem] = index
        
        return []
        



        
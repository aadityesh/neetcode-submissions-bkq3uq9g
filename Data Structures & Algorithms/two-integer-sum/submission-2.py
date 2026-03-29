class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
            Brute: 
                Stand on each element (i) and look towards its right
                for next element (j) that will sum up t target

                T/S: O(N^2)/O(1)

            
            Better:
                Sort and start from left for i and right for j
                if left > right then stop

                T/S: O(NlogN)/O(N)
        
        """

        # Brute

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return [-1, -1]


        # Better:

        hash_set = {}
        for index in range(len(nums)):
            elem = nums[index]
            difference = target - elem
            if difference in hash_set:
                return [hash_set[difference], index]

            hash_set[elem] = index
        
        return []
        



        
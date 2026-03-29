class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        tc: [1, 2, 3, 4]
        Brute:
            Stand on each element and look for the same element
            on the right side.

            T/S: O(N^2)/O(1)

        Better:
            Sort and check adjacent elements (TimSort).

            T/S: O(NlogN)/O(N)

        Optimal:
            Iterate over array and store each element in set. 
            While iterating, we check for the elem in the storage.

            T/S: O(N)/O(N)

        Fundamental:
            If duplicate: len(unique_elems) != len(input_arr)

            T/S: O(N)/O(N)

        """

        # [1, 2, 3, 3] -> TRUE
        # [1, 2, 3, 4] -> FALSE

        # [2, 1, 3, 2, 4] -> [1, 2, 2, 3, 4] -> TRUE

        # [2, 1, 3, 2, 4] -> set([2, 1, 3, 2, 4]) = [1, 2, 3, 4]

        # len(set) != len(nums) -> TRUE
        #                       -> FALSE


        unique_elems = set(nums)
        return not (len(unique_elems) == len(nums))


        
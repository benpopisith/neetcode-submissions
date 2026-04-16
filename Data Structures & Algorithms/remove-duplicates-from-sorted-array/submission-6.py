class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1. Remove duplicates from nums in-place so that each element appears only once.
        2. Return the number of unique elements denoted as 'k'

        Requirements:
        1. The order of the unique elements should remain the same as in the original array.
        2. It is not necessary to consider elements beyond the first k positions of the array.
        3. To be accepted, the first k elements of nums must contain all the unique elements.
        4. Return k as the final result.

        Thoughts:
        1. We need to traverse the array.
        2. We need to compare values that are next to each other. 
        (Because the array is already sorted in non-decreasing order)
        3. If we have a duplicate we can shift the array values 1 spot to the left.
        4. We need to then return the length of the array after all the duplicates are removed.

        """
        #      1,       2,      2,       3,      4
        #                    [i, j-1]   [j]                 
        
        # let i = pointer to where you want to input
        # let j = pointer to compare
        # if (i != j) (unique) --> set i = j, increment i, and increment j
        # else (i == j) (not unique) --> increment i and increment j


        k = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                #unique number, set i to nums[j]
                nums[k] = nums[j]
                k += 1
        return k










        
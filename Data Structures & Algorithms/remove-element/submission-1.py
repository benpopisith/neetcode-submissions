class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        two-pointer approach:

        pros:
        - can modify the array "in-place", so using this approach 
        we can accomplish this in constant space. O(1)
        - we need to traverse through the array, so using this approach
        we can accomplish this in linear time. O(n)

            2    3    4    3    4
                     [k]       [i]
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
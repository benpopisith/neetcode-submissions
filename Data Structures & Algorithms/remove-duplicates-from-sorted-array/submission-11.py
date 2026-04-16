class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
         1,    2,    3,    4,    4
             [k,j] 
        """
        # Two pointers; one pointing to where you want to input the next unique value and one to traverse the array.
        # So we know that the array is sorted so the first element is the first unique value. Can start at k = 1.

        k = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[k] = nums[j]
                k+=1
        return k


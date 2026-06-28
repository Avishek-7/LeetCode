class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            else:
                i += 1
        
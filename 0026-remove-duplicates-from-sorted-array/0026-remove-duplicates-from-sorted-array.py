class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        next_unique = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[next_unique]:
                next_unique += 1
                nums[next_unique] = nums[i]
        return next_unique + 1